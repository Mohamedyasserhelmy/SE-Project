from .models import User
from rest_framework import serializers

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'address', 'Type')