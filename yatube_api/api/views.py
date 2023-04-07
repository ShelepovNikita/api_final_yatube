
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    IsAuthenticated)
from rest_framework import viewsets

from .permissions import IsAuthorOrReadOnly
from posts.models import Group, Post, User
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer)
from .viewsets import CreateListViewSet


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly,
                          IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorOrReadOnly,
                          IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer

    def get_queryset(self):
        pk = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=pk)
        comments = post.comments.all()
        return comments

    def perform_create(self, serializer):
        serializer.save(author=self.request.user,
                        post=get_object_or_404(Post,
                                               id=self.kwargs.get("post_id")))

    def perform_update(self, serializer):
        serializer.save(author=self.request.user,
                        post=get_object_or_404(Post,
                                               id=self.kwargs.get("post_id")))


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    permission_classes = [IsAuthorOrReadOnly,
                          IsAuthenticatedOrReadOnly]
    serializer_class = GroupSerializer


class FollowViewSet(CreateListViewSet):
    permission_classes = [IsAuthorOrReadOnly,
                          IsAuthenticated]
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('following__username', )

    def get_queryset(self):
        user = self.request.user
        follows = user.follower.all()
        return follows

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            following=get_object_or_404(
                User,
                username=self.request.data.get("following")))
