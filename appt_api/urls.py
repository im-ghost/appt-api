
from django.contrib import admin
from appt_api.views import users_list,user
from django.urls import path,include

urlpatterns = [
    path('users/', users_list),
    path('users/<int:pk>', user),
]
