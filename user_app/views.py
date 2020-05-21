from django.shortcuts import render, redirect
from .models import User
import bcrypt
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def registering(request):
    errors = User.objects.user_register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    user_list_with_email = User.objects.filter(email=request.POST['email'])
    if user_list_with_email:
        messages.error(request, "That email is already registered!!")
        return redirect('/')
    pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = pw_hash,
        birthday = request.POST['birthday']
    )
    return redirect('/registered')

def registered(request):
    context = {
        'all_users' : User.objects.all()
    }
    return render(request, 'registered.html', context)

def login(request):
    errors = User.objects.user_login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/success')
        else: 
            messages.error(request, "Your email and password do not match.")
    return redirect("/")

def success(request):
    context = {
        'current_user' : User.objects.get(id=request.session['userid'])
    }
    return render(request, 'success.html', context)

def logout(request):
    del request.session['userid']
    return redirect("/")