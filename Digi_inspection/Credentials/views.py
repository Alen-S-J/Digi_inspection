from .forms import StructureForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.urls import reverse
from .models import User
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        organization = request.POST.get('organization')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')

        if password == confirm_password:
            try:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    name=name,
                    organization=organization
                )
                auth_login(request, user)
                return redirect('home')  # Redirect to the home page after successful signup
            except Exception as e:
                messages.error(request, str(e))
        else:
            messages.error(request, "Passwords do not match")
    
    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('overview')  # Redirect to the home page after successful login
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')  # Ensure 'home.html' is the correct template name

 # Ensure 'overview.html' is the correct template name
@login_required
def overview(request):
    return render(request, 'map.html')


@login_required
def newproject_view(request):
    if request.method == 'POST':
        form = StructureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your project has been created successfully!')
            return redirect('newproject')
    else:
        form = StructureForm()
    return render(request, 'newproject.html', {'form': form})

