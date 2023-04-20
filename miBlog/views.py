from django.shortcuts import render
from miBlog.models import Post
from django.views.generic import ListView,CreateView,DetailView,DeleteView,UpdateView
from django.urls import reverse_lazy


def index(request):
    return render(request,"miBlog/index.html")

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post

class AddPost(CreateView):
    model = Post
    success_url =  reverse_lazy("post-list")
    fields = '__all__'
