
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import requests
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics
from .serializers import UserSerializer,AccountSerializer
from .models import User,Account

import channels


# Create your views here.
@login_required(login_url='/loginUser/')
def room(request):
    return render(request, 'chat/room.html')
@login_required(login_url='loginUser/')
def sendMessage(request):
    if request.method == 'POST':
        message=request.POST.get("msg")
        language=request.POST.get("lang")
        username=request.user.username
        if (language=="en"):
            print(message)
            response=requests.post(url=f"http://localhost:5000/talkToBot/",json={"message":message,"username":username})
            print(response.json().__contains__("custom"))
            return JsonResponse(response.json())
        else:
            enMessage=requests.post(url=f"http://localhost:5000/languageToEnglish/{language}/{message}")
            print(enMessage.json()['text'])
            response = requests.post(url=f"http://localhost:5000/talkToBot/",json={"message": enMessage.json()['text'], "username": username})
            print(response.json())
            langResponse=requests.post(url=f"http://localhost:5000/englishToLanguage/{language}/",json=response.json())
            print(langResponse.json())
            return JsonResponse(langResponse.json())


def loginPage(request):
    return render(request,'chat/login.html')


def loginUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        request.session['bot'] = 'True'
        print(request.session.has_key('bot'))
        return render(request, 'chat/room.html')
        ...
    else:
        return render(request,'chat/login.html')


def logout_view(request):
    logout(request)
    return render(request,'chat/login.html')


class ClientIDList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        username = self.kwargs['username']
        users = User.objects.filter(username=username)
        return users


class AccountNoList(generics.ListAPIView):
    serializer_class = AccountSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        client_id = self.kwargs['Client_id']
        accounts = Account.objects.filter(Client_id=client_id)
        return accounts





