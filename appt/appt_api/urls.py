
from django.contrib import admin
from appt_api.views import Use_r,Users
from django.urls import path,include

urlpatterns = [
    path('users/', Users.as_view()),
    path('users/<int:pk>', Use_r.as_view()),
]
