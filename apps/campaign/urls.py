from django.urls import path
from apps.campaign.views import CampaignProfileView, CampaignDonationView


urlpatterns = [
    path(
        route='profile/',
        view=CampaignProfileView.as_view(),
        name="campaing-profile"
    ),
        path(
        route='donation/',
        view=CampaignDonationView.as_view(),
        name="campaing-donation"
    ),
]
