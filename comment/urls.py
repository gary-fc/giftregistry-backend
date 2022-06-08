from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from comment.api import CommentViewSet

router = routers.DefaultRouter()
router.register(r'comment', CommentViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]