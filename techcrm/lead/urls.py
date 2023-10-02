from django.urls import path , include
from .views import leadViewSet
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'leadsData',leadViewSet)


urlpatterns = [
    path('', views.lead_list , name='leads_list'),
    path(r'',include(router.urls)),
    path('<int:pk>/', views.lead_detail,name='lead_detail'),
    path('add-lead/', views.add_lead,name='add_lead'),
    path('<int:pk>/convert/', views.convert_to_client,name='leads_convert'),
    path('add-lead/',views.add_lead,name='add_lead'),
    path('<int:pk>/delete/', views.leads_delete, name='leads_delete'),
]