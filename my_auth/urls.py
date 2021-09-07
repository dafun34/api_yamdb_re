from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from my_auth.views import EmailViewSet, TokenViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('email', EmailViewSet)
router.register('token', TokenViewSet)


urlpatterns = [
    path('v1/auth/', include(router.urls)),
    path('refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),

]
