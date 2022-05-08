import py_compile
from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from dj_app import views

urlpatterns = [
    #   .index is the name of the function in views.py_compile
    #    name is the title of the page 
    # http://127.0.0.1:8000
      path("", views.home, name="HOME PAGE"),
    # http://127.0.0.1:8000/home
      path("index",views.index,name="Home Page"),
    # http://127.0.0.1:8000/review
      path("review",views.review,name="About Page"),
    #   http://127.0.0.1:8000/contact
      path("contact",views.contact,name="Contact-Us"),
    #   http://127.0.0.1:8000/service
      path("service",views.service,name="Service Page"),
    #   http://127.0.0.1:8000/signup
      path("signup",views.signUp,name="SignUp page"),
    #   http://127.0.0.1:8000/signin
      path("signin",views.signIn,name="SignUp page")
]