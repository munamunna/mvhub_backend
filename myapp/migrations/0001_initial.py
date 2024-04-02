# Generated by Django 4.2.11 on 2024-03-26 14:04

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=120, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('year', models.CharField(max_length=200)),
                ('language', models.CharField(choices=[('malayalam', 'malayalam'), ('telungu', 'telungu'), ('thamil', 'thamil'), ('english', 'english'), ('hindi', 'hindi')], default='malayalam', max_length=200)),
                ('runtime', models.FloatField()),
                ('poster_image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('description', models.CharField(max_length=200, null=True)),
                ('genres', models.ManyToManyField(to='myapp.genres')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.movies')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
