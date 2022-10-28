from dataclasses import fields
from rest_framework import serializers
from article.models import User


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= "__all__"
