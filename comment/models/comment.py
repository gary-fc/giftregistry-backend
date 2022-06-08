from datetime import datetime

from django.db import models

from campaign.models import Campaign
from user.models import User


class Comment(models.Model):
    comment = models.CharField(max_length=50)
    date = models.CharField(max_length=50, default=datetime.now().strftime("%Y-%m-%d / %H:%M:%S"))
    dona = models.CharField(max_length=50)
    user = models.ForeignKey(User, related_name="usercomment", on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, related_name="comments", on_delete=models.CASCADE)
