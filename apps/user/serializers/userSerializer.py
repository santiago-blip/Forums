from rest_framework import serializers
from apps.user.models import User

class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserGetSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','username')