from django.shortcuts import render
from Blogs.models import Category , Blog
from django.core.paginator import Paginator
from django.shortcuts import redirect


def home(request):    
    return render(request, 'home.html')

def about (request) : 
    return render (request , 'about.html')

def all_categories(request) : 
    return render (request , 'all_categories.html')

def articals (request) : 
    featured_posts = Blog.objects.filter(is_featured=True).order_by('-updated_at')
    posts = Blog.objects.filter(is_featured=False , status = 'Published')
    
    featured_posts = Blog.objects.filter(
        status='Published',
        is_featured=True
    ).order_by('-created_at')

    paginator = Paginator(featured_posts, 7)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'featured_posts' : featured_posts ,
        'posts' : posts ,
        'page_obj': page_obj, 
    }
    return render (request , 'articals.html' , context)