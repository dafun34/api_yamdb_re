from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet


router = DefaultRouter()
router.register('users',
                UserViewSet, basename='user_view_set'),
urlpatterns = [
    path('v1/', include(router.urls)),
]
