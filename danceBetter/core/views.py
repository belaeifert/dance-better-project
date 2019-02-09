from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    return render(request, 'index.html')


def registerInfo(request):
    return render(request, 'registerInfo.html')


@require_POST
def register(request):
    try:
        auxUsername = User.objects.get(username=require_POST['username'])

        if auxUsername:
            return render(request, 'url register_info', {
                'msg': 'Este nome de usuário já está sendo utilizado!'})

    except:

        try:
            auxEmail = User.objects.get(email=require_POST['email'])

            if auxEmail:
                return render(request, 'url register_info', {
                    'msg': 'Email já utilizado!'})

        except:

            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']

            newUser = User.objects.create_user(username=username, email=email, password=password)
            newUser.save()


def login(request):
    return render(request, 'login.html')
