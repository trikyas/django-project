from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    # return HttpResponse("<h1>Home Page!</h1>")
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def portfolio_view(request, *args, **kwargs):
    return render(request, "portfolio.html", {})

def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})
