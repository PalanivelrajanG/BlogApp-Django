from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post,Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm

# def home(request):
#     context = {
#         'posts':Post.objects.all()
#     }
#     return render(request,'blogapp/home.html',context)

def about(request):
    return render(request,'blogapp/about.html')

class PostListView(LoginRequiredMixin,ListView):
    model = Post
    template_name='blogapp/home.html'
    context_object_name='posts'
    ordering=['-date']

class PostDetailView(DetailView):
    model=Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comments.all().order_by('-created_at')
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     comments = Comment.objects.filter(post=post).order_by('created_at')
#     form = CommentForm()

#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.commenter = request.user
#             comment.save()
#             return redirect('post_detail', pk=pk)

#     return render(request, 'blogapp/post_detail.html', {'post': post, 'comments': comments, 'form': form})

def add_comment(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=post_id)
            comment.commenter = request.user
            comment.save()
    return redirect('blogapp-detail', pk=post_id)
