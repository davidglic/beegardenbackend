from django.contrib import admin
from .models import User, Article
from emailbot.models import VerToken

# Register your models here.

admin.site.register(User)
admin.site.register(Article)
admin.site.register(VerToken)
