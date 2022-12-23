from django.forms import ModelForm
from apps.feed.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'