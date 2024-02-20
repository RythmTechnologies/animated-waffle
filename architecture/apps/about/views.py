from django.shortcuts import render
from apps.main.mixin import HttpRequest, HttpResponse
from .models import About

# About Page Server Side Rendering
def about(request: HttpRequest) -> HttpResponse:
  context = {}
  about_model = About.objects.last()
  context['about'] = about_model
  return render(request,"pages/about.html", context)

