from django.shortcuts import render , redirect , get_object_or_404
from Blogs.models import Blog , Category
from django.db.models import Q
from .forms import RegisteretionForm
from django.contrib.auth import login , logout
from .forms import LoginForm

# Create your views here.

def category_wise_blog(request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    posts = Blog.objects.filter(
        status='Published',
        category=category
    )

    context = {
        'posts': posts,
        'category': category
    }

    return render(request, 'category_wise_blog.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug, status='Published')
    return render(request, 'post_detail.html', {'post': post})

def single_blog (request , slug_name) : 
    alone_blog = get_object_or_404(Blog, slug=slug_name, status='Published')
    context = {
        'alone_blog' : alone_blog , 
    }
    return render (request , 'single_blog.html' , context) 

def search(request):
    keyword = request.GET.get('keyword')
    posts = []

    if keyword:
        posts = Blog.objects.filter(
            Q(title__icontains=keyword) | 
            Q(short_discription__icontains = keyword) | 
            Q(content__icontains = keyword) ,
            status='Published',
        )

    return render(request, 'search.html', {
        'posts': posts,
        'keyword': keyword
    })
    
    

def register(request):
    if request.method == 'POST':
        form = RegisteretionForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home_page')
        else:
            print(form.errors)
    else:
        form = RegisteretionForm()

    return render(request, 'registeretion.html', {'form': form})


def user_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home_page')   

    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home_page')