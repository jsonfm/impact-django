from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='default.jpeg', upload_to ='profile_pics', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    blocked_user = models.ManyToManyField('self',blank=True, related_name='blocked_users', symmetrical=False)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

    def __str__(self):
        return f"{self.user.username}"


class Post(models.Model):
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')
    reposts = models.ManyToManyField(User, blank=True, related_name='post_reposts')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, editable=False)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)