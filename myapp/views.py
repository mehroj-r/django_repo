
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')

def signup(request):

    if request.POST == {}:
        return render(request, 'signup.html')

    username = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('pass')
    re_password = request.POST.get('re_pass')
    agree_term = request.POST.get('agree-term') == 'on'

    # Check if the form is valid
    if username=="" or email=="" or password=="" or re_password=="":
        messages.error(request, 'Please fill all the fields')
    elif not agree_term:
        messages.error(request, 'You have to agree to the terms and conditions')
    elif password != re_password:
        messages.error(request, 'Passwords do not match')
    else:
        # Register the user if the email is not duplicated
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email already registered in the system')
        elif User.objects.filter(username=username.lower()).exists():
            messages.error(request, 'Username already registered in the system')
        else:
            User.objects.create_user(username.lower(), email, password)
            return redirect('signin')

    return render(request, 'signup.html')

def signin(request):

    if request.POST == {}:
        return render(request, 'signin.html')

    email = request.POST.get('email')
    password = request.POST.get('your_pass')
    remember_me = request.POST.get('remember-me') == 'on'

    if email == "" or password == "":
        messages.error(request, 'Please fill all the fields')
    elif User.objects.filter(email=email).exists():

        user = User.objects.get(email=email)

        if user.check_password(password):
            auth.login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid password')
    else:
        messages.error(request, 'Email does not exist')

    if remember_me:
        pass # TODO: Do something to remember the user to avoid repeated sign in

    return render(request, 'signin.html')


def logout(request):

    auth.logout(request)

    return redirect('index')