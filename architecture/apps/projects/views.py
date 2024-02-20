from django.shortcuts import render
from apps.main.mixin import HttpRequest, HttpResponse,HttpResponseRedirect
from .models import Projects

def projects(request: HttpRequest) -> HttpResponse:
  context = {}
  project = Projects.objects.all()
  context["projects"] = project

  return render(request, "pages/project.html", context)


def single_projects(request: HttpRequest, slug:str) -> HttpResponseRedirect:
  context = {}
  project = Projects.objects.filter(slug = slug).first()
  context["project"] = project


  return render(request, "pages/project_detail.html", context)