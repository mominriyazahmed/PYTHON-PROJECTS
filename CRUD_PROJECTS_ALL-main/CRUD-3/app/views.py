from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
# Create your views here.
def home(request):
    return render(request, 'home.html')

def book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect('/show')
        except:
            pass
    else:
        form = BookForm()
    return render(request, 'index.html',{'form':form})

def show(request):
    books = Book.objects.order_by('date_published')
    return render(request, 'show.html',{'books':books})

def edit(request, bid):
    book = Book.objects.get(bid=bid)
    return render(request, 'edit.html',{'book':book})

def update(request, bid):
    book = Book.objects.get(bid=bid)
    form = BookForm(request.POST, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html',{'book':book})

def delete(request, bid):
    book = Book.objects.get(bid=bid)
    book.delete()
    return redirect('/show')