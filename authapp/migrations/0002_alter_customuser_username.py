# Generated by Django 3.2.16 on 2023-01-17 09:04

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(
                error_messages={"unique": "Пользователь с таким username уже существует."},
                help_text="Рекомендуется. Не более 150 знаков. Может содержать только символы и цифры.",
                max_length=150,
                unique=True,
                validators=[django.contrib.auth.validators.ASCIIUsernameValidator()],
                verbose_name="username",
            ),
        ),
    ]
