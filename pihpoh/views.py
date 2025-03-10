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



from rest_framework import generics
from .models import DanceLevel, Interest, Style
from .serializers import DanceLevelSerializer, IntersetSerializer, StyleSerializer

# DanceLevel Views
class DanceLevelListView(generics.ListAPIView):
    queryset = DanceLevel.objects.all()
    serializer_class = DanceLevelSerializer

class DanceLevelCreateView(generics.CreateAPIView):
    queryset = DanceLevel.objects.all()
    serializer_class = DanceLevelSerializer

class DanceLevelUpdateView(generics.UpdateAPIView):
    queryset = DanceLevel.objects.all()
    serializer_class = DanceLevelSerializer
    lookup_field = 'id'  # You can update using the 'id' field

class DanceLevelDeleteView(generics.DestroyAPIView):
    queryset = DanceLevel.objects.all()
    serializer_class = DanceLevelSerializer
    lookup_field = 'id'  # Delete using 'id'

# Interest Views
class InterestLevelListView(generics.ListAPIView):
    queryset = Interest.objects.all()
    serializer_class = IntersetSerializer

class InterestLevelCreateView(generics.CreateAPIView):
    queryset = Interest.objects.all()
    serializer_class = IntersetSerializer

class InterestLevelUpdateView(generics.UpdateAPIView):
    queryset = Interest.objects.all()
    serializer_class = IntersetSerializer
    lookup_field = 'id'

class InterestLevelDeleteView(generics.DestroyAPIView):
    queryset = Interest.objects.all()
    serializer_class = IntersetSerializer
    lookup_field = 'id'

# Style Views
class StyleLevelListView(generics.ListAPIView):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer

class StyleLevelCreateView(generics.CreateAPIView):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer

class StyleLevelUpdateView(generics.UpdateAPIView):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer
    lookup_field = 'id'

class StyleLevelDeleteView(generics.DestroyAPIView):
    queryset = Style.objects.all()
    serializer_class = StyleSerializer
    lookup_field = 'id'



# render url:-
# https://dashboard.render.com/web/srv-cv5us27noe9s73boee10/deploys/dep-cv61thvnoe9s73bppn20