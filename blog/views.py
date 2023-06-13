from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, FormView, DetailView
from .models import BlogPost, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import BlogPostForm
from django.core.paginator import Paginator
from .models import Comment

# Create your views here.

class BlogPostList(ListView):
    model = BlogPost
    template_name = 'blog/blog-grid.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostCreateView(LoginRequiredMixin, FormView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/blogpost-create.html'
    success_url = '/blog'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog-detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = Comment.objects.filter(post_id=post.id)
        num_of_comments = len(comments)
        context['comments'] = comments
        context['num_of_comments'] = num_of_comments

        return context

@login_required()
def add_comment(request, pk):
    if request.method == 'POST':
        author = request.user
        content = request.POST['content']
        post_id = pk

        comment = Comment.objects.create(author=author, content=content, post_id=post_id)
        comment.save()

        return redirect('post-detail', post_id)


