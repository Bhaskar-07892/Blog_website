from django.urls import path
from . import views

urlpatterns = [
    path('blogs/search/', views.search, name='search'),
    path('category/<int:category_id>/', views.category_wise_blog , name = 'category_wise_blog'),
    path('blogs/<slug:slug_name>/', views.single_blog , name='single_blog'),
    path('sign_in/', views.register , name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    path('newsletter/subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),

]