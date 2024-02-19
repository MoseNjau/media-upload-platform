# core/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm, ContactForm

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'core/post_list.html', {'posts': posts})

def post_detail_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'core/post_detail.html', {'post': post, 'comments': comments})

@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('core:post_list')
    else:
        form = PostForm()

    return render(request, 'core/create_post.html', {'form': form})

@login_required
def create_comment_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('core:post_detail', post_id=post_id)
    else:
        form = CommentForm()

    return render(request, 'core/create_comment.html', {'form': form, 'post': post})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            # You can add additional logic here, like sending emails, etc.
            return render(request, 'core/contact_success.html')
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})