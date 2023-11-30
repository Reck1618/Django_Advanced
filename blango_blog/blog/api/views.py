
from blog.api.serializers import PostSerializer
from blog.models import Post
from rest_framework import generics
from blog.api.permissions import IsAuthorModifyOrReadOnly, IsAdminUserForObject

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorModifyOrReadOnly | IsAdminUserForObject]
    queryset = Post.objects.all()
    serializer_class = PostSerializer