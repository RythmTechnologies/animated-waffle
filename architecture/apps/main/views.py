from django.shortcuts import render
from apps.main.mixin import HttpRequest, HttpResponse
from .models import Main, Logo

def homepage(request: HttpRequest) -> HttpResponse:
  context = {}
  model = Main.objects.all()
  context['homepages'] = model
  return render(request, "index.html", context)


def notfound(request: HttpRequest) -> HttpResponse:
  return render(request, "pages/404.html")