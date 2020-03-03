from django.urls import path
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    # path('', views.index, name='index'),
    # url(r'^(P<id>[A-Za-z]*[0-9]*)/$', getUserInfo, name="getUserInfo"),
    path('company/<str:companyID>', getCompanyInfo, name="getCompanyInfo"),
    path('<str:userID>', getUserInfo, name="getUserInfo"),
    # path('<str:id>/', getUserInfo, name="getUserInfo"),
    
    # url(r'^editProfile$', editProfile, name="editProfile"),
]