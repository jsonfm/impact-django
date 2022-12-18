from django.urls import path
from apps.campaign.views import CampaignProfileView


urlpatterns = [
    path(
        route='profile/',
        view=CampaignProfileView.as_view(),
        name="campaing-profile"
    )
]
