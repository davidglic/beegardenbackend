from rest_framework import serializers
from .models import User, Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'type', 'thumbnail', 'description', 'visible',)

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'email', 'zipcode', 'gardenarea', 'newsletter',)


class NewUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'email', 'zipcode', 'gardenarea', 'newsletter', 'password')

