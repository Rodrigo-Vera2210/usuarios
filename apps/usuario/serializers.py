from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Usuario
class UserSerializer(serializers.Serializer):
    class Meta():
        model = Usuario
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',
        ]
    