from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login as auth_login
from django.contrib import messages
from .forms import ContactForm

# Ensure user is logged in before accessing certain views
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if user has entered correct credentials
        user = authenticate(username=username, password=password) 

        if user is not None:
            # A backend authenticated the credentials
            auth_login(request, user)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html', {'error': 'Invalid credentials, please try again.'})

    # If method is GET, render the login page
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")

# Restrict access to the following views:
def about(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'about.html')
   
def services(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'services.html')
     
def contact(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
    return render(request, 'contact.html')

def intro(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'intro.html')

# this is for profile
# views.py

# from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profile.html', {'form': form})

# this is for the 
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database or send email
            form.save()
            # Add a success message
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Redirect to the contact page or any other page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


