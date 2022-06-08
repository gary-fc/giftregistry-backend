from django.db import models


class Comments(models.Model):
    comment = models.CharField(max_length=255)
    anonymous = models.BooleanField(default=False)