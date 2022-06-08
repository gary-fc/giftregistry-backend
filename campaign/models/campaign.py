from datetime import datetime

from django.db import models

from campaign.models import CampaignCategory
from user.models import User


class Campaign(models.Model):
    campaign_name = models.CharField(max_length=100, null=False)
    campaign_description = models.CharField(max_length=255, null=False)
    creation_date = models.CharField(max_length=50, default=datetime.now().strftime("%Y-%m-%d / %H:%M:%S"))
    campaign_objetive = models.IntegerField(null=False)
    ubication = models.CharField(max_length=100, null=False)
    url_campaign = models.CharField(max_length=50, unique=True, null=False)

    # CHOICES
    CAMPAIGN_TYPE_PENDIENTE = 1
    CAMPAIGN_TYPE_ACEPTADA = 2
    CAMPAIGN_TYPE_FINALIZADA = 3

    CAMPAIGN_TYPE_CHOICES = (
        (CAMPAIGN_TYPE_PENDIENTE, 'pendiente'),
        (CAMPAIGN_TYPE_ACEPTADA, 'aceptada'),
        (CAMPAIGN_TYPE_FINALIZADA, 'finalizada'),
    )

    state = models.IntegerField(choices=CAMPAIGN_TYPE_CHOICES)
    user = models.ForeignKey(
        User,
        related_name="user",
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        CampaignCategory,
        related_name="category",
        on_delete=models.CASCADE
    )
