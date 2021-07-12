from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.serializers import Serializer
from .serializers import ArticleSerializer, UserSerializer, NewUserSerializer
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from django.http import JsonResponse
import json
from rest_framework import status
from rest_framework.parsers import JSONParser

from .tokens import create_token, decode_token
import hashlib
from django.conf import settings
from .models import User, Article

# # Create your views here.
# class get_articles(generics.ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

@api_view(['GET'])
def get_articles(request, type):
    articles = Article.objects.filter(visible=True, type=type)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_an_article(request, id):
    print('get an article')
    print(id)
    try:
        article = Article.objects.get(visible=True, id=id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({'error': "Article not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def login(request):
    #take body and parse to dict
    parsed_body = request.body.decode('utf-8')
    parsed_body = json.loads(parsed_body)
    salt = settings.SALT
    print(salt)

    # pull up user
    try:
        user = User.objects.get(email=parsed_body['email'])
        
    except:
        user = None
        return Response({'error': "Invalid User ID."}, status=status.HTTP_401_UNAUTHORIZED)
    
    #validate user
    salted_pw = parsed_body['password'] + settings.SALT
    hashed_pw = hashlib.sha256(salted_pw.encode()).hexdigest()
    if user.password == hashed_pw:
    # if user.password == parsed_body['password']:
        new = {
          'email': user.email,
          'id': user.id,
          'zipcode': user.zipcode,
          'gardenarea': user.gardenarea,
          'newsletter': user.newsletter,
          'token': create_token(user.id),
          'verified': user.verified,
          'created': user.created
        }
        return Response(new, status=status.HTTP_200_OK)
    else:
        return Response({'error': "Password Mismatch."}, status=status.HTTP_403_FORBIDDEN)

    
@api_view(['POST'])
def create_user(request):
    parsed_body = request.body.decode('utf-8')
    parsed_body = json.loads(parsed_body)
    #check for created user
    try:
        user = User.objects.get(email=parsed_body['email'])
        
    except:
        user = None

    # Bounce back if email is in db
    if user != None:
        return Response({'error': "Email already registered."}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    #hash password
    salted_pw = parsed_body['password'] + settings.SALT
    hashed_pw = hashlib.sha256(salted_pw.encode()).hexdigest()
    parsed_body['password'] = hashed_pw

    serializer = NewUserSerializer(data=parsed_body) 
    if serializer.is_valid():
        serializer.save()
        
        new_user = User.objects.get(email=parsed_body['email'])
        new_serial = {
          'email': new_user.email,
          'id': new_user.id,
          'zipcode': new_user.zipcode,
          'gardenarea': new_user.gardenarea,
          'newsletter': new_user.newsletter,
          'token': create_token(new_user.id),
          'verified': new_user.verified,
          'created': new_user.created
        }
        return Response(new_serial, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['POST', 'DELETE'])
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
    # if user.password == parsed_body['password']:
    #     print("user validated.")
    
    token_bool, cargo = decode_token(parsed_body['token'])
    if token_bool and cargo['user'] == user.id:
        #delete user
        print(request.method)
        if request.method == 'DELETE':
            print("delete recognized")
            # user.objects.delete()
            User.objects.get(email=parsed_body['email']).delete()
            return Response({'Message': "User Deleted."})
        
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
            print(parsed_body)
            salted_pw = parsed_body['password'] + settings.SALT
            hashed_pw = hashlib.sha256(salted_pw.encode()).hexdigest()
            if hashed_pw == user.password:
                salted_new = parsed_body['new'] + settings.SALT
                hashed_new = hashlib.sha256(salted_new.encode()).hexdigest()
                user.password = hashed_new
                # user.password = parsed_body['new']
                
            else:
                return Response({'error': "Password Mismatch."}, status=status.HTTP_403_FORBIDDEN)

        else:
            print('invalid')
            return Response({'error': "Invalid User Edit Request."}, status=status.HTTP_400_BAD_REQUEST)

        updated_user = user.save()
        new = {
          'email': user.email,
          'id': user.id,
          'zipcode': user.zipcode,
          'gardenarea': user.gardenarea,
          'newsletter': user.newsletter,
          'token': parsed_body['token'],
          'verified': user.verified,
          'created': user.created
        }
        
        return Response(new, status=status.HTTP_200_OK)
    else:
        return Response({'error': "Invalid Authorization Token."}, status=status.HTTP_401_UNAUTHORIZED)


from django.db.models import Sum, Avg
@api_view(['GET'])
def get_info(request, id):
    #search user and vertoken
    try: 
        print(id)
        user = User.objects.get(id=id)
        print(user.zipcode)
        print(type(user.zipcode))
        gardens = User.objects.filter(zipcode=user.zipcode)
        print(gardens.aggregate(Sum('gardenarea')))
        all_gardens = User.objects.all()
        response = {
            'created': user.created,
            'zipcode': user.zipcode,
            'gardenarea': user.gardenarea,
            'gardencount_local': gardens.count(),
            'totalsqft_local': gardens.aggregate(Sum('gardenarea'))['gardenarea__sum'],
            'avgsqft_local': gardens.aggregate(Avg('gardenarea'))['gardenarea__avg'],
            'gardencount_total': all_gardens.count(),
            'totalsqft_total': all_gardens.aggregate(Sum('gardenarea'))['gardenarea__sum'],
            'avgsqft_total': all_gardens.aggregate(Avg('gardenarea'))['gardenarea__avg']
        }
        return Response(response, status=status.HTTP_200_OK)
    except:
        return Response({'error': "No garden exists with this ID."}, status=status.HTTP_400_BAD_REQUEST)
        

