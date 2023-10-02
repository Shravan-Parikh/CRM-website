from django.contrib.auth.forms import UserCreationForm , User
from django.shortcuts import render, redirect
# from .forms import PostForm
from rest_framework import viewsets
from.models import Userprofile
from.serializer import UserSerializer
from django.contrib.auth import authenticate
from django.http import JsonResponse
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer


from django.http import HttpResponse



def login_view(request , method='POST'):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User exists and credentials are correct
            return JsonResponse({'message': 'Login successful!'})
        else:
            # Invalid credentials or user does not exist
            return JsonResponse({'message': 'Invalid username or password.'}, status=401)

    return JsonResponse({'message': 'Invalid request method.'}, status=400)
    
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user=form.save()

            Userprofile.objects.create(user=user)

            return redirect('/log-in/')
    else:
        form = UserCreationForm()

    return render(request,'userprofile/signup2.html' , {'form':form})
 

