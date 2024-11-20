from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def login(request):

    if request.user.is_authenticated:
        return redirect('/temperature/')

    elif request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            print('user logged in')
            return redirect('/temperature/')

        else:
            print("########### User doesn't exist")
            messages.error(request, "Wrong User Credentials")
            return render(request, 'login.html')

    else:
        return render(request,'login.html')


def register(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmedPassword = request.POST['confirmedPassword']

        if password == confirmedPassword:
            if User.objects.filter(username = username).exists():
                print('################# Username already used')
                messages.error(request, 'Username is already taken')
                return render(request, 'register.html')

            elif User.objects.filter(email = email).exists():
                print('############### email already used')
                messages.error(request, 'Email has already been used')
                return render(request, 'register.html')

            else:
                user = User.objects.create_user(username = username, password = password, email = email, first_name = first_name, last_name = last_name)
                user.save();
                print('user created')
                return redirect(login)
        else:
            print('################ Password doesnt match')
            messages.error(request, "Password doesn't match")
            return render(request, 'register.html')


    else:
        return render( request,'register.html')

def logout(request):
    auth.logout(request)
    return render(request, 'login.html')