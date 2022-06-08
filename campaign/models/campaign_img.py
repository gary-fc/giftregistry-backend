from django.db import models

from campaign.models import Campaign


class CampaignImg(models.Model):
    img = models.FileField(upload_to="media")
    is_portada = models.BooleanField()
    campaign = models.ForeignKey(
        Campaign,
        related_name="imgs",
        on_delete=models.CASCADE
    )