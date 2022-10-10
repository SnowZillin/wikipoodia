from django.shortcuts import render
from django.http import HttpResponse
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def CSS(request):
    return render(request, 'encyclopedia/CSS.html')

def Django(request):
    return render(request, 'encyclopedia/Django.html')

def Git(request):
    return render(request, 'encyclopedia/Git.html')

def HTML(request):
    return render(request, 'encyclopedia/HTML.html')

def Python(request):
    return render(request, 'encyclopedia/Python.html')

