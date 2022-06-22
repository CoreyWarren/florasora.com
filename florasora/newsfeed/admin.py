from django.contrib import admin
from newsfeed.models import Post, Comment, Artwork, CodeProject, CodeDescriptionBlock


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Artwork)
admin.site.register(CodeProject)
admin.site.register(CodeDescriptionBlock)
