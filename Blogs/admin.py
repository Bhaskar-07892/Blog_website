from django.contrib import admin
from .models import Category , Blog , NewsletterSubscriber

# Register your models here.

class Blog_Admin (admin.ModelAdmin) : 
    
    prepopulated_fields = {"slug" : ('title' ,)}
    search_fields = ('id' , 'title' , 'category__category_name' , 'status')
    list_display = ('title' , 'category' , 'status' , 'is_featured')
    list_editable = ('is_featured' ,)
    

admin.site.register(Category)
admin.site.register(Blog , Blog_Admin)
admin.site.register(NewsletterSubscriber)