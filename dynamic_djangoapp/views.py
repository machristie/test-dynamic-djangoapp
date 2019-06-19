from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def hello_world(request):
    return render(request, "dynamic_djangoapp/hello.html")
