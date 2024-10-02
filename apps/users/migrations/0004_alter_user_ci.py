# Generated by Django 5.1.1 on 2024-10-02 14:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20240913_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ci',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='La cédula de identidad consta de 7 a 8 números, o 7 a 8 números y un complemento separado por guiones EJ 5567756 o 5567756-2B', regex='^([0-9]{7,8})(-[A-Z0-9]{2})?$')], verbose_name='C.I.'),
        ),
    ]