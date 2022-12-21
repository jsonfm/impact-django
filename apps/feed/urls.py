from django.urls import path
from apps.feed.views import (
    FeedView, 
    SearchFeedView, 
    PostEditView,
    PostCreateView,
    StoryDetailView
)


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
    path(
        route='post/edit/',
        view=PostEditView.as_view(),
        name="post-edit"
    ),
    path(
        route='post/create/',
        view=PostCreateView.as_view(),
        name="post-create"
    ),
    path(
        route='story/detail/',
        view=StoryDetailView.as_view(),
        name="story-detail"
    ),
]
