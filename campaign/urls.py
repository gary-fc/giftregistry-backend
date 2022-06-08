from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from campaign.api import CampaignViewSet, CampaignCategoryViewSet, CampaignImgViewSet

router = routers.DefaultRouter()
router.register(r'campaign', CampaignViewSet)
router.register(r'campaign_category', CampaignCategoryViewSet)
router.register(r'campaign_img', CampaignImgViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
