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


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer

@method_decorator(csrf_exempt, name='dispatch')
class LoginAPIView(APIView):
    authentication_classes = []  # Disable authentication for login
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                "message": "Login successful",
                "token": access_token,
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
