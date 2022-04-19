from comments.api.serializers import CommentsSerializer
from comments.models import Comment
from config.settings import REST_LEVEL_COMMENT  # noqa
from rest_framework import serializers

from ..models import Post


class PostsSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField("_get_first_line_comments_for_post")

    def _get_first_line_comments_for_post(self, post):  # noqa
        return [
            CommentsSerializer(comment).data
            for comment in Comment.objects.filter(
                post=post,
                level__lte=REST_LEVEL_COMMENT,
                active=True,
            )
        ]

    class Meta:
        model = Post
        fields = "__all__"
