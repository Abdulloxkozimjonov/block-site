from django.shortcuts import render , redirect
from .models import *
from main.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required



@login_required(login_url="login_url")
def index_view(request):
    context={
        "courses":Courses.objects.all().order_by("-id")[:3],
        "about":About.objects.all(),
        "baner": Baner.objects.all().order_by("-id")[:4],
        "user":request.user,
    }
    return render(request,"index.html",context)


@login_required(login_url="login_url")
def about_view(request):
    context={
        "about": About.objects.all().order_by("-id")[:4],
        "user":request.user
    }
    return render(request,"about.html",context)


@login_required(login_url="login_url")
def courses_view(request):
    context={
        "courses":Courses.objects.all().order_by("-id")[:2],
        "user": request.user
    }
    return render(request,"courses.html",context)


@login_required(login_url="login_url")
def price_view(request):
    context = {
        "price": Price.objects.all().order_by("-id")[:4],
        "user": request.user
    }
    return render(request,"price.html",context)


@login_required(login_url="login_url")
def videos_view(request):
    context = {
        "video":Video.objects.all(),
        "user": request.user,
        "category":Category.objects.all()
    }
    return render(request,"videos.html",context)


@login_required(login_url="login_url")
def contact_view(request):
    context = {
        "user": request.user
    }
    return render(request,"contact.html",context)


@login_required(login_url="login_url")
def my_profile_view(requset, pk):
    context={
        "profile":User.objects.last(),
        "user" : User.objects.get(pk=pk)
    }
    return render(requset,"myprofile.html",context)


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request, usr)
            return redirect('index_url')
    return render(request,"login.html")


def register_view(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        User.objects.create_user(
            username=username,
            password=password,
        )
        return redirect('index_url')
    return render(request,"register.html")


def log_out_view(request):
    logout(request)
    return redirect("login_url")


@login_required(login_url="login_url")
def edit_user_view(request,pk):
    user= User.objects.get(pk=pk)
    if request.method == "POST":
        username=request.POST['username']
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        bio=request.POST.get('bio')
        phone_number=request.POST.get('phone_number')
        password=request.POST.get('password')
        confirm_password=request.POST.get('cofirm_password')
        user.username=username
        if first_name is not None:
            user.first_name=first_name
        if last_name is not None:
            user.last_name=last_name
        if email is not None:
            user.email =email
        if bio is not None:
            user.bio=bio
        if phone_number is not None:
            user.phone_number = phone_number
        if password is not None:
            if password == confirm_password:
                user.set_password(password)
        user.save()
        return redirect("my_profile_url", user.id)
    context={
        'user':user
    }
    return render(request,"edit.html",context)


@login_required(login_url="login_url")
def create_contact_view(request):
    if request.method == "POST":
        your_name = request.POST['your_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        message = request.POST['message']
        subject = request.POST['subject']
        contact = Contact.objects.create(
            name=your_name,
            email=email,
            phone_number=phone_number,
            message=message,
            subject=subject,
        )
        return redirect("contact_url")
    return render(request,"contact.html")