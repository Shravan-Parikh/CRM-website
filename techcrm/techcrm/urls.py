from django.contrib import admin
from django.contrib.auth import views
from django.urls import path , include
# from userprofile.serializer import ur
from .views import About
from userprofile.views import signup


urlpatterns = [
    path('',  views.LoginView.as_view(template_name='userprofile/login2.html'),name='index' ),
    
    path('sign-up/',signup,name='signup'),
    path('About/',About,name='About'),
    path("users/v1/",include('userprofile.urls')),
    path("users/v1/",include('lead.urls')),
    path("users/v1/",include('clients.urls')),

    path('dashboard/leads/',include('lead.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('dashboard/clients/',include('clients.urls')),
    path('log-in/',views.LoginView.as_view(template_name='userprofile/login2.html'), name='login'),
    path('log-out/',views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
]
