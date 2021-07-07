from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment_name', 'comment_email', 'date_comment', 'comment_published')
    list_editable = ('comment_published',)
    list_display_links = ('id', 'comment_name')


admin.site.register(Comment, CommentAdmin)
