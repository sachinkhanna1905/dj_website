from multiprocessing import context
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    
    # we need to import httpresponse from django.shortcuts
    # return HttpResponse("This is Home Page")
    # now we want to render Temples files so we need to import render
    return render(request,'home.html')

def index(request):
    
    return render(request,'index.html') 


def review(request):

    # return HttpResponse("This is About Page")  
      return render(request,'review.html')  

def contact(request):
    
    # return HttpResponse("This is Contact Page")  
      return render(request,'contact.html')  

def service(request):
    
    return render(request,'service.html')  


def signUp(request):
    
    return render(request,'sign_up.html') 


def signIn(request):
    
    return render(request,'sign_in.html')   
   