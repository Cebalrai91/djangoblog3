from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('zjawiska/', views.zjawiska, name='zjawiska'),
    path('mglawice/', views.mgławice, name='mgławice'),
    path('planety/', views.planety, name='planety'),
    path('nowe/', views.nowe, name='nowe'),





]

