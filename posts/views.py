from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CommentForm, PostForm
from .models import Comment, Post


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect("feed")
    else:
        form = PostForm()

    return render(request, "posts/create_post.html", {"form": form})


def feed(request):
    posts = Post.objects.all()

    return render(
        request,
        "posts/feed.html",
        {"posts": posts}
    )

@login_required
def add_comment(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

    return redirect("feed")

@login_required
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect("feed")

@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if post.author != request.user:
        return redirect("feed")

    if request.method == "POST":
        form = PostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if form.is_valid():
            form.save()
            return redirect("feed")
    else:
        form = PostForm(instance=post)

    return render(
        request,
        "posts/edit_post.html",
        {"form": form, "post": post}
    )


@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if post.author != request.user:
        return redirect("feed")

    if request.method == "POST":
        post.delete()

    return redirect("feed")