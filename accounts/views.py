from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import authenticate
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializers import *
from .utils import * 

@api_view(['POST'])
def signup(request):
    serializers = SignupSerializers(data=request.data)
    if serializers.is_valid(raise_exception=True):
        User.objects.create_user(
            username=serializers.validated_data["username"],
            email=serializers.validated_data["email"],
            password=serializers.validated_data["password"]
        )
        
        return Response({"message": "Registration successfully!"}, status=status.HTTP_201_CREATED)
    
    
@api_view(["POST"])
def signin(request):
    serializers = SigninSerializers(data=request.data)
    serializers.is_valid(raise_exception=True)
    
    user = authenticate(
        request,
        username=serializers.validated_data["username"],
        password=serializers.validated_data["password"]
    )
    if user is not None:
        token = get_tokens_for_user(user)
        return Response({"message": "Login successful", "access_token": token["access"], "refresh": token["refresh"]}, status=status.HTTP_200_OK)