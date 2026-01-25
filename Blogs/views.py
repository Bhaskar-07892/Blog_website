from django.http import HttpResponseRedirect
from django.shortcuts import render , redirect , get_object_or_404
from Blogs.models import Blog , Category , CommentModel
from django.db.models import Q
from .forms import RegisteretionForm
from django.contrib.auth import login , logout
from django.core.mail import send_mail
from django.contrib import messages
from .forms import LoginForm , NewsletterForm 
from .email_host_password import Email_Host_Password , Email_Sender

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

from Blogs.models import Blog, CommentModel

def single_blog(request, slug_name):
    blog = get_object_or_404(Blog, slug=slug_name, status='Published')

    comments = CommentModel.objects.filter(blog=blog).order_by('-created_at')
    comment_count = comments.count()

    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_text = request.POST.get('comment')

            if comment_text:
                CommentModel.objects.create(
                    user=request.user,
                    blog=blog,
                    comment=comment_text
                )
                return redirect(request.path)
        else:
            return redirect('login')

    context = {
        'alone_blog': blog,
        'comments': comments,
        'comment_count': comment_count
    }
    return render(request, 'single_blog.html', context)

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

def newsletter_subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)

        if form.is_valid():
            subscriber = form.save()

            # Confirmation email
            send_mail(
                subject='Thanks for subscribing!',
                message='You are successfully subscribed to ModernBlog 🎉',
                from_email=Email_Sender,
                recipient_list=[subscriber.email],
                fail_silently=False,
            )

            messages.success(request, "Subscription successful! Check your email.")
        else:
            messages.error(request, "Invalid or already subscribed email.")

    return redirect(request.META.get('HTTP_REFERER'))