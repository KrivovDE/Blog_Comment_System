from comments.api.views import CommentsViewSet
from posts.api.views import PostViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentsViewSet)
