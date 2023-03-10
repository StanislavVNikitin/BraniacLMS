# Generated by Django 3.2.16 on 2023-01-16 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0008_data_migration_teachers"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="lesson",
            options={"ordering": ("course", "num"), "verbose_name": "Lessons", "verbose_name_plural": "Lessons"},
        ),
        migrations.AlterModelOptions(
            name="news",
            options={"ordering": ("-created",), "verbose_name": "News", "verbose_name_plural": "News"},
        ),
    ]
