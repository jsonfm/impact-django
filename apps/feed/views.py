from django.views.generic import TemplateView, ListView
from apps.feed.models import Post


class FeedView(ListView):
    template_name = 'feed/index.html'
    model = Post
    paginate_by = 10
    context_object_name = "posts"


class SearchFeedView(TemplateView):
    template_name = 'feed/search.html'


class PostEditView(TemplateView):
    template_name = 'feed/postedit.html'


class PostCreateView(TemplateView):
    template_name = 'feed/postcreate.html'


class StoryDetailView(TemplateView):
    template_name = 'feed/storydetail.html'
