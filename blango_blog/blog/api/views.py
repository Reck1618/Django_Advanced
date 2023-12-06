
from blog.api.serializers import PostSerializer, UserSerializer, PostDetailSerializer, TagSerializer
from blog.models import Post, Tag
from blango_auth.models import User
from rest_framework import generics, viewsets
from blog.api.permissions import IsAuthorModifyOrReadOnly, IsAdminUserForObject
from rest_framework.decorators import action
from rest_framework.response import Response

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action in ("list", "create"):
            return PostSerializer
        return PostDetailSerializer

class UserDetail(generics.RetrieveAPIView):
    lookup_field = "email"
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    @action(detail=True, methods=["get"], name="Posts with the tag")
    def posts(self, request, pk=None):
        tag = self.get_object()
        posts = tag.posts.all()
        serializer = PostSerializer(posts, many=True, context={"request": request})
        return Response(serializer.data)