from django.shortcuts import render , redirect ,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .serializer import leadSerializer
from . forms import AddLeadForm
from .models import Lead
from rest_framework import viewsets
from django.http import JsonResponse

from clients.models import Client

# Create your views here.
class leadViewSet(viewsets.ModelViewSet):
    queryset=Lead.objects.all()
    serializer_class=leadSerializer

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             # User exists and credentials are correct
#             return JsonResponse({'message': 'Login successful!'})
#         else:
#             # Invalid credentials or user does not exist
#             return JsonResponse({'message': 'Invalid username or password.'}, status=401)

#     return JsonResponse({'message': 'Invalid request method.'})
                        
@login_required
def lead_list(request):
    leads= Lead.objects.filter(created_by=request.user , converted_to_client=False)

    return render(request,'lead/leads_list2.html',{
        'leads':leads
    })

@login_required
def lead_detail(request,pk):
    lead = Lead.objects.filter(created_by=request.user).get(pk=pk)

    return render(request,'lead/lead_detail2.html',{
        'lead' : lead
    })

@login_required
def leads_delete(request,pk):
    lead = get_object_or_404(Lead,created_by=request.user,pk=pk)
    lead.delete()

    return redirect('leads_list')


@login_required
def add_lead(request):
    if request.method =='POST':
        form = AddLeadForm(request.POST)

        if form.is_valid():
            lead= form.save(commit=False)
            lead.created_by = request.user
            lead.save()

            return redirect('dashboard')
        
    else:
        form = AddLeadForm()

    return render(request,'lead/add_lead2.html',{
        'form' : form
    })

@login_required
def convert_to_client(request,pk):
    lead = get_object_or_404(Lead,created_by=request.user,pk=pk)

    client = Client.objects.create(
        name=lead.name,
        email=lead.email,
        description=lead.description,
        created_by=request.user,
    )

    lead.converted_to_client = True
    lead.save()

    return redirect('leads_list2')