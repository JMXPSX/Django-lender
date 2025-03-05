from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import CreateUserForm, LoginForm, CreateLenderForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Lender

def home(request):
    return render(request, 'webapp/index.html')

# - Register user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        
    context = {'form':form}
    return render(request, 'webapp/register.html', context=context)

# - Login user
def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")

    context = {'form':form}
    return render(request, 'webapp/login.html', context=context)

# - Dashboard
@login_required(login_url='login')
def dashboard(request):

    return render(request, 'webapp/dashboard.html')

# - lender Entry Form
@login_required(login_url='login')
def lender_entry(request):

    form = CreateLenderForm()
    if request.method == "POST":
        form = CreateLenderForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('lender-results'))
    
    context = {'form':form}
    return render(request, 'webapp/lender-entry.html', context=context)

# - lender Results Page
@login_required(login_url='login')
def lender_results(request):

    lenders = Lender.objects.all()
    context = {'lenders': lenders}
    return render(request, 'webapp/lender-results.html', context=context)

# - Logout user
def logout(request):

    auth.logout(request)
    return redirect("login")