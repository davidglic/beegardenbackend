from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['PUT'])
def send_verification(request, id):
    print('Sending verification email for user: ' + str(id))
    return Response({'message': 'Verification E-mail Sent.'}, status=status.HTTP_200_OK)
