from django.urls import path
from .views import BlogPostList, PostCreateView, BlogDetailView, add_comment

urlpatterns = [
    path('', BlogPostList.as_view(), name='blog-posts'),
    path('new/', PostCreateView.as_view(), name='create-post'),
    path('post/<int:pk>', BlogDetailView.as_view(), name='post-detail'),
    path('comment/<int:pk>', add_comment, name='add-comment')
]