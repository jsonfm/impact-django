from django.urls import path
from apps.feed.views import FeedView


urlpatterns = [
    path(
        route='',
        view=FeedView.as_view(),
        name="feed"
    )
]
