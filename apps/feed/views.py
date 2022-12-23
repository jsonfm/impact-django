from django.views.generic import TemplateView, ListView, CreateView
from apps.feed.models import Post
from apps.feed.forms import PostForm


class FeedView(ListView):
    template_name = 'feed/index.html'
    model = Post
    paginate_by = 10
    context_object_name = "posts"


class SearchFeedView(TemplateView):
    template_name = 'feed/search.html'


class PostEditView(TemplateView):
    template_name = 'feed/postedit.html'


class PostCreateView(CreateView):
    template_name = 'feed/postcreate.html'
    form_class = PostForm


class StoryDetailView(TemplateView):
    template_name = 'feed/storydetail.html'
