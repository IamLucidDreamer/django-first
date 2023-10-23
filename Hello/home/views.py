from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # return HttpResponse('<p style="color:blue;font-size:46px;">Im a big, blue, <strong>strong</strong> paragraph</p>')
    context = {
        'variable1' : "this is sent",
        'variable2' : "this is sent 2"
    }
    return render(request , "index.html",context )
def about(request):
    return render(request , "about.html" )

def services(request):
    return render(request , "services.html" )

def contact(request):
    if request.method == 'POST' : 
        email = request.POST.get("email")
        password = request.POST.get("password")
        contact = Contact(email = email , password = password, date= datetime.today())
        contact.save()
        messages.success(request , "Your Data has been saved.")
    return render(request , "contact.html" )