from dataclasses import fields
from rest_framework import serializers
from article.models import Article


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields= ['id', 'title', 'content']
