
from django.conf.urls import url, include

from . import views

app_name = 'dynamic_djangoapp'
urlpatterns = [
    url(r'^hello/', views.hello_world, name="home"),
]
