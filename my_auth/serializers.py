from rest_framework import serializers
from my_auth.models import TokenEmail


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('email',)
        model = TokenEmail


class TokenSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        email = attrs.get('email')
        confirmation_code = attrs.get('confirmation_code')
        if TokenEmail.objects.filter(
                email=email,
                confirmation_code=confirmation_code).exists():
            return attrs
        raise serializers.ValidationError('Not found emeil or '
                                          'confirmation_code!')

    class Meta:
        fields = ('email', 'confirmation_code')
        model = TokenEmail
