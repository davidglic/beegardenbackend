from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.serializers import Serializer
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from django.http import JsonResponse
import json
from rest_framework import status
from rest_framework.parsers import JSONParser


from .models import User, Article

# # Create your views here.
# class get_articles(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

@api_view(['GET'])
def get_articles(request, type):
    articles = Article.objects.filter(visible=True, type=type)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def login(request):
    #take body and parse to dict
    parsed_body = request.body.decode('utf-8')
    parsed_body = json.loads(parsed_body)

    # pull up user
    try:
        user = User.objects.get(email=parsed_body['email'])
        serializer = UserSerializer(user)
    except:
        user = None
        return Response({'error': "Invalid User ID."})
    
    #validate user
    if user.password == parsed_body['password']:
        #return user
        return Response(serializer.data)
    else:
        return Response({'error': "Password Mismatch."})

    



@api_view(['POST'])
def update_user(request):
    # takes email, pw, object to be changed and new value
    # {email: '', password: '', object: 'email, zipcode, gardenarea, newsletter, password', new: ''}
    #take body and parse to dict
    parsed_body = request.body.decode('utf-8')
    parsed_body = json.loads(parsed_body)

    # pull up user
    try:
        user = User.objects.get(email=parsed_body['email'])
        
    except:
        user = None
        return Response({'error': "Invalid User ID."})
    
    #validate user
    if user.password == parsed_body['password']:
        #update user
        if parsed_body['object'] == "email":
            user.email = parsed_body['new']
            
        elif parsed_body['object'] == "zipcode":
            user.zipcode = parsed_body['new']
            
        elif parsed_body['object'] == "gardenarea":
            user.gardenarea = parsed_body['new']
            
        elif parsed_body['object'] == "newsletter":
            user.newsletter = parsed_body['new']
            
        elif parsed_body['object'] == "password":
            user.password = parsed_body['new']
            
        else:
            print('invalid')
            return Response({'error': "Invalid User Edit Request."})

        updated_user = user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data)
    else:
        return Response({'error': "Password Mismatch."})

