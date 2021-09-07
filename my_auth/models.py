from django.db import models


class TokenEmail(models.Model):
    email = models.EmailField(blank=False, verbose_name='Email')
    confirmation_code = models.CharField(max_length=100,
                                         blank=True,
                                         verbose_name='Код поддтверждения')
    data_registrate = models.DateTimeField(auto_now=True,
                                           verbose_name='Дата регистрации')

    class Meta:
        verbose_name = 'Почта-код подтверждения'
        verbose_name_plural = 'Почта-коды подтверждения'
