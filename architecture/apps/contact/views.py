from django.shortcuts import render, redirect
from apps.main.mixin import HttpRequest, HttpResponseRedirect
from .models import Contact, CompanyInfo


def contact_form(request: HttpRequest) -> HttpResponseRedirect:
  context = {}
  company = CompanyInfo.objects.first()
  context["company"] = company
  if request.method == "POST":
    name = request.POST.get("input-name")
    surname = request.POST.get("input-surname")
    email = request.POST.get("input-email")
    message = request.POST.get("input-message")

    if name and surname and email and message:
      contact = Contact.objects.create(name = name, surname = surname, email = email, message = message)
      contact.save()
      return redirect("contact")
    else:
      return redirect("contact")

  return render(request, "pages/contact.html",context)

