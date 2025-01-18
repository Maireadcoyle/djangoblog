from django.shortcuts import render
from django.http import HttpResponse

def my_blog(request):
    return HttpResponse("Hello, Blog!")


def home(request):
    return render(request, 'blog/home.html')  # Create a home.html template

def my_blog(request):
    return render(request, 'blog.html')  # Create a blog.html template

