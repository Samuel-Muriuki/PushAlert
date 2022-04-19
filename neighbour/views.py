from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render
from . forms import UpdateUserForm, UpdateUserProfileForm, UserRegisterForm, HoodForm, BusinessForm, PostForm
from django.contrib.auth.decorators import login_required
from .models import NeighbourHood, Business, Post, Profile

# Create your views here.
def index(request):
    return render(request, 'all-neighbour/home.html')


def register(request):
    if request.user.is_authenticated:
        # redirect user to the profile page
        return redirect('home')
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, "registration/register.html", {'form': form})

@login_required(login_url='login')
def hoods(request):
    current_user = request.user
    hoods = NeighbourHood.objects.all()
    return render(request, "all-neighbour/hoods.html", {'hoods': hoods, 'current_user': current_user})

