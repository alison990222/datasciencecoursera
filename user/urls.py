from django.urls import path
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    # path('', views.index, name='index'),
    url(r'^$', getUserInfo, name="getUserInfo"),
    url(r'company$', getCompanyInfo, name="getCompanyInfo"),
    url(r'^editProfile$', editProfile, name="editProfile"),
]