# accounts/serializers.py
from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'company', 'year', 'role', 'is_staff', 'is_superuser', 'date_joined')
        read_only_fields = ('id', 'is_staff', 'is_superuser', 'date_joined')

    def create(self, validated_data):
        # Ensure password is hashed
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        # If password present, hash it
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
