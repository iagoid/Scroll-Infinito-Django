from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Post

class PostView(ListView):
    model = Post
    paginate_by = 4
    context_object_name = 'posts'
    template_name = 'posts.html'
    ordering = ['title']

