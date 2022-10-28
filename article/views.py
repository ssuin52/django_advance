from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import article
from article.serializers import ModelSerializer
from article.models import Article

class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ModelSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        article = ModelSerializer(data=request.data)
        if article.is_valid():
            article.save(author=request.user)
            return Response(article.data, status=status.HTTP_200_OK)
        else:
            return Response(article.errors, status=status.HTTP_400_BAD_REQUEST)

