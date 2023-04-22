from django.shortcuts import render
from miBlog.models import Post
from django.views.generic import ListView,CreateView,DetailView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request,"miBlog/index.html")

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model = Post

class AddPost(LoginRequiredMixin, CreateView):
    model = Post
    success_url =  reverse_lazy("post-list")
    fields = '__all__'

class UpdatePost(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = '__all__'

class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post-list")
    

