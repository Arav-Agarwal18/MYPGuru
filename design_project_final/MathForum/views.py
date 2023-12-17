from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Comment
from .forms import PostForm, CommentForm
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from django.contrib.auth import get_user_model

def post_list(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid(): 
            post = form.save(commit=False)
            if hasattr(request.user, 'teacher'):  
                user = get_user_model().objects.get(teacher=request.user.teacher)
                post.author = user
                post.is_verified = True
            else:
                post.author = request.user
            post.save()
            messages.success(request, 'Post submitted successfully.')
            return redirect('MathForum:post_list')
        else:
            messages.error(request, 'Post submission failed.')
    else:
        form = PostForm()
    posts = Post.objects.all()
    if hasattr(request.user, 'teacher'): 
        unverified_posts = Post.objects.filter(is_verified=False)
        return render(request, 'math.html', {'posts': posts, 'form': form, 'unverified_posts': unverified_posts})
    else:
        return render(request, 'math.html', {'posts': posts, 'form': form})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)
    comment_form = CommentForm()
    post_form = PostForm()
    if request.method == 'POST':
        if 'comment_submit' in request.POST:  
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                print(comment)
                return redirect('MathForum:post_detail', pk=post.pk)
        elif 'post_submit' in request.POST: 
            post_form = PostForm(request.POST)
            if post_form.is_valid():
                new_post = post_form.save(commit=False)
                new_post.author = request.user
                new_post.save()
                return redirect('MathForum:post_detail', pk=new_post.pk)

    return render(request, 'math_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form, 'post_form': post_form})