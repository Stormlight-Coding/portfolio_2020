from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
    return render(request, "portfolio/index.html")

def algo(request):
    return render(request, "portfolio/algo.html")

def barry(request):
    return render(request, "portfolio/barry.html")

def list(request):
    return render(request, "portfolio/list.html")

def numbers(request):
    return render(request, "portfolio/numbers.html")

def strata(request):
    return render(request, "portfolio/strata.html")

def support(request):
    return render(request, "portfolio/support-people.html")

def wedding(request):
    return render(request, "portfolio/wedding.html")
