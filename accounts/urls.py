from django.urls import path
from .views import *


urlpatterns = [
    path("signup/", signup, name="signup"),
    path("signin/", signin, name="signin"),
    path("change_password/", change_password, name="change_password"),
    path("create_otp/", create_otp, name="create_otp"),
    path("reset_password/", reset_password, name="reset_password")
]
