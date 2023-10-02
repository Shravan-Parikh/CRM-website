from django.contrib.auth.decorators import login_required
from django.shortcuts import render , get_object_or_404
from rest_framework import viewsets
from .models import Client
from .serializer import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer


# Create your views
@login_required
def clients_list(request):
    clients = Client.objects.filter(created_by=request.user)

    return render( request,'clients/clients_list2.html',{
        'clients': clients
    })

@login_required
def clients_detail(request,pk):
    client = get_object_or_404(Client,created_by=request.user, pk=pk)

    return render( request,'clients/clients_detail2.html',{
        'client': client
    })
