from django.contrib import admin
from my_auth.models import TokenEmail


class TokenEmailAdmin(admin.ModelAdmin):
    pass


admin.site.register(TokenEmail, TokenEmailAdmin)
