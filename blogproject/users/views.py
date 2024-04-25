from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"{username} Account Created Successfully. Login Now!!")
            return redirect('blogapp-home')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html',{'form':form})

def custom_logout(request):
    logout(request)
    messages.success(request,'You were Logged out!!')
    return redirect('blogapp-home')

@login_required
def profile(request):
    return render(request, 'users/profile.html')