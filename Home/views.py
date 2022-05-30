from xmlrpc.client import DateTime
from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
     context = {
          "variable1":"Prince is founder of the website",
          "variable2":"Prince is the CEO of the website" 
     }     
     return render(request, 'index.html',context)

def about (request):
     return render(request, 'about.html')
def services (request):
     return render(request, 'services.html')
def contact (request):
     if request.method == "POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          phone = request.POST.get('phone')
          desc = request.POST.get('desc')
          contact = Contact(name=name, email=email, phone=phone, desc=desc, date= DateTime.today())
          contact.save() 
          messages.success(request, 'Your message has been sent')      
     return render(request, 'contact.html')
 