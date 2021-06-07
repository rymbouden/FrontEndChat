from django.conf.urls import url
from django.urls import path, include
from .views import room,sendMessage,loginPage,loginUser,logout_view,ClientIDList,AccountNoList







urlpatterns = [
    path('room/', room),
    path('loginUser/sendMessage',sendMessage),
    path('loginUser/',loginPage),
    path('loginUser/login',loginUser),
    path('logout/',logout_view),
    path('accounts/', include('django.contrib.auth.urls')),
    url('^users/(?P<username>.+)/$', ClientIDList.as_view()),
    url('^accounts/(?P<Client_id>.+)/$', AccountNoList.as_view()),



]