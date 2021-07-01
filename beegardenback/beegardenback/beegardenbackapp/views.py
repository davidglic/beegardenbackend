from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.serializers import Serializer
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions

from .models import User, Article

# # Create your views here.
# class get_articles(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

@api_view(['GET'])
def get_articles(request, type):
    articles = Article.objects.filter(visible=True, type=type)
    print(articles)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
    # return Response('True return')