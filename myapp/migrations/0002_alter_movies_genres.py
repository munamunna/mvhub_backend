# Generated by Django 4.2.11 on 2024-03-29 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='genres',
            field=models.ManyToManyField(null=True, to='myapp.genres'),
        ),
    ]
