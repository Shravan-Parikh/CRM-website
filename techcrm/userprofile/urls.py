
from django.urls import path , include

from userprofile.views import UserViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'profile',UserViewSet)

urlpatterns = [
    path('',include(router.urls))
]