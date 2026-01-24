from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    
    category_name = models.CharField(max_length=50 , unique=True)
    created_at = models.DateTimeField(auto_now_add=True) # update only one time
    updated_at = models.DateTimeField(auto_now=True) # update many time
    
    class Meta : 
        verbose_name_plural = "Categories"
    
    def __str__(self) : 
        return self.category_name

   
STATUS_CHOICE = (
    ("Draft", "Draft"),
    ("Published", "Published")
)
    

class Blog(models.Model) :
    
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=150 , unique = True ) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y%m%d')
    short_discription = models.CharField(max_length=300)
    content = models.CharField(max_length=2000)
    status = models.CharField(choices=STATUS_CHOICE, default="Draft", max_length=20)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email 
    
class CommentModel(models.Model) : 
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='comments')
    blog = models.ForeignKey(Blog , on_delete=models.CASCADE , related_name='comments')
    comment = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment