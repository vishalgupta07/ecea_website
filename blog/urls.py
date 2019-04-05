# -*- coding: utf-8 -*-
# @Author: gvishal
# @Date:   2019-03-31 00:26:01
# @Last Modified by:   vishalgupta07
# @Last Modified time: 2019-04-05 19:04:01
from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, EventListView
from . import views 
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('events/', EventListView.as_view(), name='blog-events'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
]

# <app>/<model>_<viewtype>.html/