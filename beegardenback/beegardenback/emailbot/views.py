from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import serializers, status
from django.core.mail import send_mail
from .serializers import VerTokenSerializer
import json

import random

from django.conf import settings
from .models import User, VerToken


# Create your views here.
@api_view(['PUT'])
def send_verification(request, id):
    
    # query user and check if already verified.
    try: 
        user = User.objects.get(id=id)
    except:
        return Response({'error': "Invalid User Submitted."}, status=status.HTTP_400_BAD_REQUEST)
    
    #delete token if previous exists
    try:
        VerToken.objects.get(email=user.email).delete()
    except:
        pass

    #create code store in DB
    vertoken = {'email': user.email, 'vertoken': random.randrange(100000, 999999)}
    serializer = VerTokenSerializer(data=vertoken)
    if serializer.is_valid():
        serializer.save()

    #send code to member.
    send_mail(
        'Little Bee Gardens: E-mail verification code',
        'Verification code: ' + str(vertoken['vertoken']),
        'settings.EMAIL_HOST_USER',
        [user.email],
        fail_silently=False,
        )
    return Response({'message': 'Verification E-mail Sent.'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def accept_verification(request):
    #search user and vertoken
    try: 
        
        parsed_body = request.body.decode('utf-8')
        parsed_body = json.loads(parsed_body)
        user = User.objects.get(id=parsed_body['id'])
        vertoken = VerToken.objects.get(email=user.email)
    except:
        return Response({'error': "Invalid Verification info Submitted."}, status=status.HTTP_400_BAD_REQUEST)
    # verify token

    if vertoken.vertoken == parsed_body['vertoken']:
        #update DB
        user.verified = True
        user.save()
        VerToken.objects.get(email=vertoken.email).delete()
        #serialize user
        return Response({'message': 'Email Verified.'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': "Invalid Verification Token."}, status=status.HTTP_401_UNAUTHORIZED)
    

    