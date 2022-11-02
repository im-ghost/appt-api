
from django.contrib import admin
from appt_api.views import users_list,user_create
from django.urls import path,include

urlpatterns = [
    path('users/', user_create),
    path('users/list', users_list),
]
