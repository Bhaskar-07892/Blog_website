from django.urls import path
from . import views

urlpatterns = [
    path('blogs/search/', views.search, name='search'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/<int:category_id>/', views.category_wise_blog , name = 'category_wise_blog'),
    path('<slug:slug_name>/', views.single_blog , name='single_blog'),
]