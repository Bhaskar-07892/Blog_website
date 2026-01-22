from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    
    path('dashboard/categories/' , views.categories , name='categories'),
    path('dashboard/categories/add/' , views.add_category , name='add_category'),
    path('dashboard/categories/edit/<int:pk>/' , views.edit_category , name='edit_category'),
    path('dashboard/categories/delete/<int:pk>/' , views.delete_category , name='delete_category'),
    
    path('dashboard/posts/' , views.posts , name='posts'),
    path('dashboard/posts/add/' , views.add_post , name='add_post'),
    path('dashboard/posts/edit/<int:pk>/' , views.edit_post , name='edit_post'),
    path('dashboard/posts/delete/<int:pk>/' , views.delete_post , name='delete_post'),
    
    path('dashboard/user/' , views.user , name='user1'),
    path('dashboard/user/add/' , views.add_user , name='add_user'),
    path('dashboard/user/edit/<int:pk>/' , views.edit_user , name='edit_user'),
    path('dashboard/user/delete/<int:pk>/' , views.delete_user , name='delete_user'),
]