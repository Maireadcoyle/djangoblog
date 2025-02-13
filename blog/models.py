from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# STATUS = ((0, "Draft"), (1, "Published"))

#create models here


#createupdatemodel stops you from having to repeat code in different models
class CreateUpdateModel(models.Model):
    creation_date = models.DateTimeField(default=timezone.now)
    Update_date = models.DateTimeField(auto_now=True)
#abstract=true will make sure the code above dosnt create a table
    class Meta:
        abstract = True

# category model
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# tag model
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Post(CreateUpdateModel):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    # post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    status = models.CharField(  #fixed using AI
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )
   # creation_date = models.DateTimeField(auto_now_add=True) no need for these two lines now due to createupdatemodel parent
   # Update_date = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    hero_image = models.ImageField(upload_to="post", default="post/sample.jpg")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
        )
    excerpt = models.TextField(blank=True)
    categories = models.ManyToManyField(Category, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')
    # pillow needs to be installed for hero image abovepython

    # def __str__(self):  updated below
    #    return self.title

    def __str__(self):
        return f"{self.title} | written by {self.author}"   

    # The - prefix on created_on indicates the posts are displayed in descending order of creation date. If no leading - is used, then the order is ascending, and if a ? prefix is used, then the order is randomised.
    class Meta:
       ordering = ['-creation_date']


class Comment(CreateUpdateModel):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # on delete=models.casecade when we delete the post the comment is also deleted
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_comments")
    is_comment_approved = models.BooleanField(default=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')


    def __str__(self):
       return f'Comment by {self.author} on {self.post}'  

    class Meta:
        ordering = ['creation_date']
     
   
#is_draft status = models.IntegerField(choices=STATUS, default=0)







