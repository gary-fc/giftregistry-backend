from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from donation.api import DonationViewSet

router = routers.DefaultRouter()
router.register(r'donation', DonationViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]