from rest_framework import viewsets
import django_filters
from rest_framework.generics import get_object_or_404
from users.models import User
from users.serializers import UserSerializer
from users.permissions import IsOwnerOrAdmin, IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['username', ]
    lookup_field = 'username'
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin, ]
    http_method_names = ['get', 'post', 'head', 'patch', 'delete']

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        if self.kwargs.get('username') == 'me':
            self.kwargs['username'] = self.request.user.username
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(queryset, **filter_kwargs)

        self.check_object_permissions(self.request, obj)
        return obj

    @property
    def allowed_methods(self):
        if (self.request.method == 'DELETE'
                and self.kwargs.get('username') == 'me'):
            self.http_method_names = ['get', 'post', 'head', 'patch']
        return self._allowed_methods()
