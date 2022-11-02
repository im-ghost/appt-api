from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from appt_api.serializer import userSerializer
from django.http import JsonResponse
from appt_api.models import User
# Create your views here.
@api_view(['GET','POST'])
def users_list(request):
  if request.method == "GET":
    users = User.objects.all()
    serialized = userSerializer(users,many=True);
    return Response(serialized.data)
  elif request.method == "POST":
    serializer = userSerializer(data=request.data)
  
    if serializer.is_valid():
     serializer.save()
     print(serializer)
     return Response(serializer.data)
    else:
     return Response(serializer.errors)
@api_view(["GET","DELETE","PUT","PATCH"])
def user(request,pk):
  try:
   user = User.objects.get(pk=pk)
  except:
    return Response({
      "error":"user not found"
    },status=status.HTTP_404_NOT_FOUND)
  if request.method == "GET":
    serializer = userSerializer(user)
    return Response(serializer.data)
  elif request.method == "PUT":
    serializer = userSerializer(user,data=request.data)
  
    if serializer.is_valid():
     serializer.save()
     print(serializer)
     return Response(serializer.data)
    else:
     return Response(serializer.errors)
  elif request.method == "DELETE":
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    
    