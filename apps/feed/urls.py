from django.urls import path
from apps.feed.views import FeedView, SearchFeedView


urlpatterns = [
    path(
        route='',
        view=FeedView.as_view(),
        name="feed"
    ),
    path(
        route='search/',
        view=SearchFeedView.as_view(),
        name="feed-search"
    ),
]
