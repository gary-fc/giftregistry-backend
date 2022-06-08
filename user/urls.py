from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from user.api import UserViewSet, LoginViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
    path('login/', LoginViewSet.as_view(), name='token_obtain_pair'),
]