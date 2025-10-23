from rest_framework import serializers 
from django.contrib.auth.models import User


class SignupSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        
        
class SigninSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
class ResetPasswordSerializers(serializers.Serializer):
    username = serializers.CharField()
    new_password = serializers.CharField()
    otp = serializers.CharField()
    
class SendOtpSerializers(serializers.Serializer):
    otp = serializers.CharField() 