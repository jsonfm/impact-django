from django.contrib import admin
from apps.feed.models import Profile, Post


admin.site.register(Profile)
admin.site.register(Post)