from rest_framework import serializers
from .models import VerToken

class VerTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerToken
        fields = ('id', 'email', 'vertoken')



