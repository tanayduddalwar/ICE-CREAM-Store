from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from myapp.models import Contact
import logging


def home(request):
    return render(request, "index.html")

def aboutus(request):
    if request.method == "POST":
        try:
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            desc = request.POST.get("desc")
            contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
            contact.save()
            

        # Save the contact object to the database
        except IntegrityError as e:
            logging.error(f"Error saving contact: {str(e)}")

    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def service(request):
    return render(request, "service.html")
def familypack(request):
    return render(request,"familypack.html")
