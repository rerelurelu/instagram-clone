from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, CreateView, DetailView
from django import forms

from posts.models import Post, Comment


class PostList(ListView):
    template_name = 'posts/post_list.html'
    model = Post


class PostCreate(CreateView):
    template_name = 'posts/post_create.html'
    model = Post
    fields = ['image', 'description', 'author']
    success_url = '/'


class CommentForm(forms.Form):
    comment = forms.CharField()


class PostDetail(DetailView):
    template_name = 'posts/post_detail.html'
    model = Post

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = Comment(
                author = request.user,
                post = self.get_object(),
                text = comment_form.cleaned_data['comment']
            )
            comment.save()
        else:
            raise Exception
        return redirect(reverse('posts:post_detail', args=[self.get_object().id]))