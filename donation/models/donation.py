from datetime import datetime

from django.db import models

from campaign.models import Campaign
from user.models import User


class Donation(models.Model):
    campaign_donation = models.FloatField()
    gift_registry_donation = models.FloatField()
    total_donation = models.FloatField()
    invited = models.BooleanField()
    donation_date = models.CharField(max_length=50, default=datetime.now().strftime("%Y-%m-%d / %H:%M:%S"))
    userdonation = models.ForeignKey(
        User,
        related_name="userdonation",
        on_delete=models.CASCADE

    )
    campaign = models.ForeignKey(
        Campaign,
        related_name="donations",
        on_delete=models.CASCADE
    )
