from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def blog(request):
    if request.method  == 'POST':
        form = BlogForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect('/show')
        except:
            pass
    else:
        form = BlogForm()
    return render(request, 'index.html',{'form':form})

def show(request):
    blogs = Blog.objects.order_by('-date_published')
    return render(request, 'show.html',{'blogs':blogs})

def edit(request, bid):
    blog = Blog.objects.get(bid=bid)
    return render(request, 'edit.html',{'blog':blog})

def update(request, bid):
    blog = Blog.objects.get(bid=bid)
    form = BlogForm(request.POST, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html',{'blog':blog})

def delete(request, bid):
    blog = Blog.objects.get(bid=bid)
    blog.delete()
    return redirect('/show')