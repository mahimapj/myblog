from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost

# Home page - list all blogs
def index(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/index.html', {'posts': posts})

# Add new blog
def create_post(request):
    if request.method == 'POST':
        BlogPost.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            content=request.POST['content'],
            image=request.FILES.get('image')
        )
        return redirect('index')
    return render(request, 'blog/post_form.html')

# View blog details
def view_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# Edit blog
def edit_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.author = request.POST['author']
        post.content = request.POST['content']
        if request.FILES.get('image'):
            post.image = request.FILES.get('image')
        post.save()
        return redirect('index')
    return render(request, 'blog/post_form.html', {'post': post})

# Delete blog
def delete_post(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    post.delete()
    return redirect('index')
