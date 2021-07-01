# Generated by Django 3.2.5 on 2021-07-01 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('type', models.CharField(max_length=20)),
                ('thumbnail', models.TextField()),
                ('description', models.TextField(max_length=280)),
                ('visible', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField(max_length=5)),
                ('gardenarea', models.IntegerField(max_length=3)),
                ('newsletter', models.BooleanField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]