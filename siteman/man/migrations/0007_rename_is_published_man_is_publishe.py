# Generated by Django 4.2.1 on 2024-06-07 19:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("man", "0006_category_man_cat"),
    ]

    operations = [
        migrations.RenameField(
            model_name="man",
            old_name="is_published",
            new_name="is_publishe",
        ),
    ]