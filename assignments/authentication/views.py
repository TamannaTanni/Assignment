from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from pyexpat.errors import messages


# Create your views here.
def login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            print('user logged in')
            return redirect('/temperature/')


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

        user = User.objects.create_user(username = username, password = password, email = email, first_name = first_name, last_name = last_name)
        user.save();
        print('user created')
        return redirect('/login/')


    else:
        return render( request,'register.html')
