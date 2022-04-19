from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import Comment


@admin.register(Comment)
class CommentAdminView(DraggableMPTTAdmin):

    fields = ['post', 'name', 'email', 'body', 'active', 'parent']
    readonly_fields = ['created', 'updated']
    mptt_level_indent = 20

