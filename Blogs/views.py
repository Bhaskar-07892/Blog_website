from django.shortcuts import render , redirect , get_object_or_404
from Blogs.models import Blog , Category

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

