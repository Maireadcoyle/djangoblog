from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    model = Post

    
def home(request):
    return render(request, 'blog/home.html')  # Create a home.html template

def my_blog(request):
    return render(request, 'blog.html')  # Create a blog.html template

