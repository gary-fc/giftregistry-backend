from django.db import models


class CampaignCategory(models.Model):
    campaign_category = models.CharField(max_length=100, null=False)
    