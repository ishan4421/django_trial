from django.shortcuts import render
from django.http import HttpResponse
from .forms import Investor
from django.urls import reverse


# Create your views here.

def index_html(request):
    return HttpResponse(
        "<html>"
        "<head><title>hello world</title></head>"
        "<body><p>one paragraph</p>"
        "<a href='/first'>click me</a>"                               
        "<script type='text/javascript'>"
        "console.log('first log');"  # Fixed the string syntax here
        "alert('first alert'); "
        "document.write('<p>hello world</p>');"
        "</script>"
        "<p>cncd</p>"
        "<script type='text/javascript'>"
        "alert('second alert'); "
        "document.write('<p>hello world</p>');"
        "</script>"
        "</body></html>"
    )

#in above i am redirecting to first page


def Investorform(request):
    if request.method == 'GET':
        form = Investor()  # Create an instance of the form
        return HttpResponse(form.as_table())
    
def first(request):
    return render(request, 'trial/first.html') 