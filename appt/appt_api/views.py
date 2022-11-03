from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from appt_api.serializer import userSerializer
from django.http import JsonResponse
from appt_api.models import User

from rest_framework.views import APIView
class Users(APIView):
  def get(self, request):
    users = User.objects.all()
    serialized = userSerializer(users,many=True);
    return Response(serialized.data)
  def post(self, request):
    serializer = userSerializer(data=request.data)
  
    if serializer.is_valid():
     serializer.save()
     print(serializer)
     return Response(serializer.data)
    else:
     return Response(serializer.errors)
class Use_r(APIView):
  def get_user_by_pk(self,pk):
    try:
      user = User.objects.get(pk=pk)
      return user
    except:
      return Response({
        "error":"user not found"
      },status=status.HTTP_404_NOT_FOUND)
  def get(self,request,pk):
    user = self.get_user_by_pk(pk)
    serializer = userSerializer(user)
    return Response(serializer.data)
  def delete(self, request,pk):
    user = self.get_user_by_pk(pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  def put(self, request,pk):
    user = self.get_user_by_pk(pk)
    serializer = userSerializer(user,data=request.data)
  
    if serializer.is_valid():
     serializer.save()
     print(serializer)
     return Response(serializer.data)
    else:
     return Response(serializer.errors)