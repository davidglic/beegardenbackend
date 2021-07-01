from rest_framework import serializers
from .models import User, Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'type', 'thumbnail', 'description', 'visible',)