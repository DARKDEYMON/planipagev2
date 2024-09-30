# Generated by Django 5.1.1 on 2024-09-13 21:22

from django.db import migrations
from django.contrib.postgres.operations import TrigramExtension, UnaccentExtension, CITextExtension


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options'),
    ]

    operations = [
        TrigramExtension(),
        UnaccentExtension(),
        CITextExtension()
    ]
