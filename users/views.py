from rest_framework.generics import GenericAPIView
from rest_framework import response, status
from django.contrib.auth import authenticate

from .serializer import RegisterSerializer


class RegisterAPIView(GenericAPIView):
  serializer_class = RegisterSerializer
  
  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    
    if serializer.is_valid():
      serializer.save()
      return response.Response(serializer.data, status.HTTP_201_CREATED)
    return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class LogInAPIView(GenericAPIView):
  
  def post(self, request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = authenticate(username=email, password=password)
    
    
    if user:
      pass