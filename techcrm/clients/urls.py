from django.urls import path , include
from .views import ClientViewSet
from rest_framework import routers
from . import views 

clientrouter=routers.DefaultRouter()
clientrouter.register(r'ClientData',ClientViewSet)

urlpatterns=[
    path('',views.clients_list,name='clients_list'),
    path('',include(clientrouter.urls)),
    path('<int:pk>',views.clients_detail,name='clients_detail')

    
]