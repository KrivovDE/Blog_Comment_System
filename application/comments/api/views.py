from rest_framework import viewsets

from ..models import Comment
from .serializers import CommentsSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
