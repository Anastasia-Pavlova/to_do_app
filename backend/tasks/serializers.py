from rest_framework import serializers

from .models import *


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=20)

class CreateTaskSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField(required=False)
    user_id = serializers.IntegerField()

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

class TaskSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField(required=False)
    user = UserSerializer()

    def create(self, validated_data):
        return Task.objects.create(**validated_data)