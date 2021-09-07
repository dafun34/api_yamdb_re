from django.urls import path, include
from rest_framework.routers import DefaultRouter
from titles.views import (TitlesViewSet,
                          CategoryViewSet,
                          GenreViewSet,
                          ReviewViewSet,
                          CommentViewSet)

router = DefaultRouter()
router.register("titles", TitlesViewSet, basename='Title')
router.register("genres", GenreViewSet, basename='Genre')
router.register("categories", CategoryViewSet, basename='Category')
router.register(
    r'titles/(?P<title_id>[0-9]+)/reviews',
    ReviewViewSet,
    basename='Review'
)
router.register(
    r'titles/(?P<title_id>[0-9]+)/reviews/(?P<review_id>[0-9]+)/comments',
    CommentViewSet,
    basename='Comment'
)

urlpatterns = [
    path('v1/', include(router.urls))
]
