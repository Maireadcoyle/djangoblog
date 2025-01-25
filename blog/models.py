from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

#create models here
class Post(models.Model):
    # post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    Update_date = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
)
    
    def __str__(self):
        return self.title

    class Meta:
       ordering = ['-creation_date']

   #replaced by is_draft status = models.IntegerField(choices=STATUS, default=0)
