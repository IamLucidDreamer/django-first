from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('<p style="color:blue;font-size:46px;">Im a big, blue, <strong>strong</strong> paragraph</p>')
    context = {
        'variable1' : "this is sent",
        'variable2' : "this is sent 2"
    }
    return render(request , "index.html",context )
def about(request):
    return HttpResponse('this is about')

def services(request):
    return HttpResponse('this is services')

def contact(request):
    return HttpResponse('this is contact')