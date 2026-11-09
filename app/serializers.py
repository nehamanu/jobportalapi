from rest_framework import serializers
from app.models import Job
from django.contrib.auth.models import User

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields="__all__"
        read_only_fields=['posted_by']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            'username',
            'password',
            'email'
        ]

    def create(self, validated_data):
        u = User.objects.create_user(**validated_data)
        u.save()
        return u
