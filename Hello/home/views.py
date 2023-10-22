from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<p style="color:blue;font-size:46px;">Im a big, blue, <strong>strong</strong> paragraph</p>')