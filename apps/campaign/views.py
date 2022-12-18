from django.views.generic import TemplateView


class CampaignProfileView(TemplateView):
    template_name = "campaign/profile.html"