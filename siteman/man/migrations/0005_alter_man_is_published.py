# Generated by Django 4.2.1 on 2024-06-06 18:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("man", "0004_rename_is_publishe_man_is_published"),
    ]

    operations = [
        migrations.AlterField(
            model_name="man",
            name="is_published",
            field=models.BooleanField(
                choices=[(0, "Черновик"), (1, "Опубликовано")], default=0
            ),
        ),
    ]
