from comments.api.serializers import CommentsSerializer
from comments.models import Comment
from config.settings import REST_LEVEL_COMMENT  # noqa
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import Post
from .serializers import PostsSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostsSerializer

    @action(detail=True, methods=["get"], url_path="get_other_comments")
    def get_other_comments(self, request, pk):
        data_ = [
            CommentsSerializer(comment).data
            for comment in Comment.objects.filter(
                post=pk,
                level__gte=REST_LEVEL_COMMENT,
                active=True,
            ).order_by("parent")
        ]
        return Response(status=status.HTTP_200_OK, data=data_)
