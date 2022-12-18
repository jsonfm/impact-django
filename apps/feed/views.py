from django.views.generic import TemplateView


class FeedView(TemplateView):
    template_name = 'feed/index.html'


class SearchFeedView(TemplateView):
    template_name = 'feed/search.html'
