from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Post, Comment




class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    fields = ('title', 'body','picture')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'




class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    fields = ('title', 'body','picture')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'blog/post_comment.html'
    fields =('post','body')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



