from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework import viewsets, status
from rest_framework_simplejwt.tokens import RefreshToken

from api_yamdb.settings import EMAIL_HOST_USER
from my_auth.models import TokenEmail
from my_auth.serializers import EmailSerializer, TokenSerializer
import uuid

from users.models import User


def get_user_token(user):
    token = RefreshToken.for_user(user)
    return str(token.access_token)


class EmailViewSet(viewsets.ModelViewSet):
    queryset = TokenEmail.objects.all()
    serializer_class = EmailSerializer
    http_method_names = ['post', ]
    permission_classes = [AllowAny, ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        confirmation_code = uuid.uuid4()
        recipient_email = serializer.validated_data.get('email')
        User.objects.get_or_create(
            email=recipient_email,
            username=recipient_email
        )
        send_mail(
            subject='confirm_code',
            message=f'Hi, your confirm_code is {confirmation_code}.',
            from_email=EMAIL_HOST_USER,
            recipient_list=[recipient_email],
            fail_silently=False,
        )
        self.perform_create(serializer, confirmation_code)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def perform_create(self, serializer, confirmation_code):
        serializer.save(confirmation_code=confirmation_code)


class TokenViewSet(viewsets.ModelViewSet):
    queryset = TokenEmail.objects.all()
    serializer_class = TokenSerializer
    http_method_names = ['post', ]
    permission_classes = [AllowAny, ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        email = serializer.validated_data.get('email')
        confirmation_code = serializer.validated_data.get('confirmation_code')
        user = get_object_or_404(User, email=email,
                                 confirmation_code=confirmation_code)
        token = get_user_token(user)

        return Response({'token': token},
                        status=status.HTTP_201_CREATED,
                        headers=headers)
