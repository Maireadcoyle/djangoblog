from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(creation_date__lte=timezone.now()).order_by('-creation_date')
    template_name = "blog/index.html"
    paginate_by = 6 # what does this mean?
    
#    model = Post
def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )

    
def home(request):
    return render(request, 'blog/home.html')  # Create a home.html template

def my_blog(request):
    return render(request, 'blog.html')  # Create a blog.html template

