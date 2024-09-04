from django.apps import AppConfig


class ManConfig(AppConfig):
    verbose_name = 'Мужики'
    default_auto_field = "django.db.models.BigAutoField"
    name = "man"

class CategoryConfig(AppConfig):
    verbose_name = 'Категории'
    default_auto_field = "django.db.models.BigAutoField"
    name = "man"
