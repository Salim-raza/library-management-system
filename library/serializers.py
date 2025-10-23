from rest_framework import serializers
from .models import *


class BookAddUpdateDeleteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        
