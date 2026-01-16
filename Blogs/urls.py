from django.urls import path
from . import views

urlpatterns = [
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/<int:category_id>/' , views.category_wise_blog , name='category_wise_blog' )
]