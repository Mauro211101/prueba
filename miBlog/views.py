from django.shortcuts import render
from miBlog.models import Post
from django.views.generic import ListView,CreateView,DetailView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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

class UpdatePost(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("post-list")
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get("pk")
        return Post.objects.filter(publisher=user_id, id=post_id).exists()
    
    def handle_no_permission(self):
        return render(self.request,"Account/not_found.html")



class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post-list")

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get("pk")
        return Post.objects.filter(publisher=user_id, id=post_id).exists()
    
    def handle_no_permission(self):
        return render(self.request,"Account/not_found.html")
    

