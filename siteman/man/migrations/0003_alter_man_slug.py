# Generated by Django 4.2.1 on 2024-06-06 14:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("man", "0002_alter_man_options_man_slug_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="man",
            name="slug",
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]