from django.shortcuts import render
# from django.http import httpResponse
from django.views import View 

class HomeView(View):
    def get(self,request):
        return render(request,'home.html')



from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import SignupSerializer

User = get_user_model()  # Get the custom user model

class SignupListView(generics.ListAPIView):
    queryset = User.objects.all()  # Now it correctly references CustomUser
    serializer_class = SignupSerializer

class SignupCreateView(generics.CreateAPIView):  
    queryset = User.objects.all()  
    serializer_class = SignupSerializer
