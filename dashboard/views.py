from django.shortcuts import get_object_or_404, redirect, render
from Blogs.models import Blog, Category 
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm , BlogPostForm , AddUserForm, EditUserForm
from django.utils.text import slugify
from django.contrib.auth.models import User
    
# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    context = {
        'category_count': Category.objects.count(),
        'post_count': Blog.objects.count(),
        'published_count': Blog.objects.filter(status='Published').count(),
        'recent_posts': Blog.objects.order_by('-created_at')[:5]
    }
    return render(request, 'dashboard/dashboard.html', context)


def categories(request) : 
    return render (request , 'dashboard/categories.html')


def add_category (request) : 

    
    if request.method == 'POST' : 
        form =  CategoryForm(request.POST)
        
        if form.is_valid() : 
            form.save()
            return redirect (dashboard)      
 
    form = CategoryForm()
    context = {
        'form' : form
    }
    
    return render (request , 'dashboard/add_category.html' , context)

def edit_category (request , pk):
    category = get_object_or_404(Category , pk = pk)
    if request.method == 'POST' : 
        form = CategoryForm(request.POST , instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
        
    form = CategoryForm(instance=category)
    
    context = {
        'form' : form ,
        'category' : category
    }
    return render (request , 'dashboard/edit_category.html' , context)

def delete_category (request , pk):
    category = get_object_or_404(Category , pk = pk)
    category.delete()
    return redirect ('categories')

def posts (request) :
    blog_post_all = Blog.objects.all()
    context = {
        'blog_post_all' : blog_post_all
    }
    return render (request , 'dashboard/posts.html' , context)

def add_post(request):

    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.status = "Draft"

            post.save()

            # UNIQUE SLUG with ID
            post.slug = f"{slugify(post.title)}-{post.id}"
            post.save(update_fields=['slug'])

            return redirect('posts')

    else:
        form = BlogPostForm()

    return render(request, 'dashboard/add_post.html', {'form': form})

def edit_post (request , pk):
    post = get_object_or_404(Blog , pk=pk)
    if request.method == 'POST' : 
        form = BlogPostForm(request.POST , request.FILES , instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data['title']
            post.slug = f"{slugify(title)}-{str(post.id)}"
            post.save()
            return redirect('posts')
        
    form = BlogPostForm(instance=post)
    context = {
        'form' : form , 
        'post' : post
    }
    return render (request , 'dashboard/edit_post.html' , context)

def delete_post (request , pk) : 
    post = get_object_or_404(Blog , pk=pk)
    post.delete() 
    return redirect('posts' )   


def user (request) : 
    users = User.objects.all()
    context = {
        'users' : users
    }
    return render (request , 'dashboard/user_info.html' , context)

def add_user(request) : 
    if request.method == 'POST' : 
        form = AddUserForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('user1')
    form = AddUserForm()
    
    context = {
        'form' : form
    }
    return render(request , 'dashboard/add_user.html' , context)

def edit_user(request , pk) : 
    user_edit = get_object_or_404(User , pk=pk)
    if request.method == 'POST' :
        form = EditUserForm(request.POST , instance = user_edit) 
        if form.is_valid:
            form.save()
            return redirect ('user1')
    form = EditUserForm(instance = user_edit)
    context = {
        'form' : form
    }
    return render(request , 'dashboard/edit_user.html' , context)

def delete_user(request , pk) :
    user_delete = get_object_or_404(User , pk=pk)
    user_delete.delete()
    return redirect('user1')