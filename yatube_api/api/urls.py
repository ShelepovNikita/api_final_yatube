from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CommentViewSet,
    FollowViewSet,
    GroupViewSet,
    PostViewSet)

VERSION_API = 'v1/'

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet)
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet,
                   basename='comment')
router_v1.register('groups', GroupViewSet)
router_v1.register('follow', FollowViewSet, basename='follow')


urlpatterns = [
    path(f'{VERSION_API}', include('djoser.urls.jwt')),
    path(f'{VERSION_API}', include(router_v1.urls)),
]
