from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

#create models here


#createupdatemodel stops you from having to repeat code in different models
class CreateUpdateModel(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    Update_date = models.DateTimeField(auto_now=True)
#abstract=true will make sure the code above dosnt create a table
    class Meta:
        abstract = True


     

class Post(CreateUpdateModel):
    # post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
   # creation_date = models.DateTimeField(auto_now_add=True) no need for these two lines now due to createupdatemodel parent
   # Update_date = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    hero_image = models.ImageField(upload_to="post", default="post/sample.jpg")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
        )
    excerpt = models.TextField(blank=True)

    class Comment(CreateUpdateModel):
        text = models.TextField()
        post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # on delete=models.casecade when we delete the post the comment is also deleted
        author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
        )
        is_comment_approved = models.BooleanField(default=False)
     
    def __str__(self):
        return self.title

    class Meta:
       ordering = ['-creation_date']

   #replaced by is_draft status = models.IntegerField(choices=STATUS, default=0)
