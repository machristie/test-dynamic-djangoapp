from django.apps import AppConfig


class DynamicDjangoAppConfig(AppConfig):
    name = 'dynamic_djangoapp'
    label = name
    verbose_name = "Test Dynamic Django App"
