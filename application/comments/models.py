from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Comment(MPTTModel):
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=200, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    parent = TreeForeignKey(
        "comments.Comment",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ("pk",)
        indexes = [
            models.Index(fields=["post"]),
            models.Index(fields=["parent"]),
        ]

    def __str__(self):
        return f"{self.name} для {self.post}"
