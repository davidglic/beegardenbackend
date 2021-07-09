from django.db import models
from django.db.models.query import ValuesListIterable


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    type = models.CharField(max_length=20)
    thumbnail= models.TextField()
    description = models.TextField(max_length=280)
    visible = models.BooleanField()

    # title = Title of article displayed
    # content = Content of article as Str that will be parsed to html on frontend.
    # type = short str so frontend knows how to parse. news, howto, article, etc.
    # thumbnail= thumbnail image url for preview
    # description = short description to be viewed on preview.
    # visible = api will only send out visible articles

    def __str__(self):
        return self.title

class User(models.Model):
    email = models.CharField(max_length=100)
    zipcode = models.PositiveBigIntegerField()
    gardenarea = models.PositiveSmallIntegerField()
    newsletter = models.BooleanField()
    password = models.CharField(max_length=100)
    verified = models.BooleanField(default=False, blank=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email