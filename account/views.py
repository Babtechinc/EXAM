from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import profile

def er404(response):

    return render(response,'404-page.html',context={})

# Create your views here.
@login_required(login_url='/account/login')
def home(response):
    print(response.user)
    if profile.objects.filter(profileUser=response.user):
        UserProfile = profile.objects.get(profileUser=response.user)
        response.session["UserRole"] = UserProfile.roleUser
        response.session["UserProfileimg"] = UserProfile.profileImg.url
        return render(response, 'index.html', context={})
    # if reponse.user.is_authenticated:
    #     print(';fkleejl')
    else:
        print("heol")
        print("heol")

    return render(response,'404-page.html',context={})

def login_in(response):
    if response.method == "POST":
        print('here')
        username = response.POST['username']
        password = response.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(response, user)

            return redirect("home")


        else:
            messages.error(response, 'ERROR')

    # No backend authenticated the credentials
    return render(response,'sign-in.html',context={})