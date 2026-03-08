from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def home(request):
    #return render(request)
    return HttpResponse("Recipes Home page")

def redirect_to_homepage(request):
    return redirect("homepage/")

def create_recipe(request):
    return HttpResponse("Create Recipe view")




