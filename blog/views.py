from django.shortcuts import render
from django.views import generic
from django.utils import timezone
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(creation_date__lte=timezone.now()).order_by('-creation_date')
    template_name = "post_list.html"
#    model = Post

    
def home(request):
    return render(request, 'blog/home.html')  # Create a home.html template

def my_blog(request):
    return render(request, 'blog.html')  # Create a blog.html template

