from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .form import BookForm


def book_list(request):
    books=Book.objects.all()
    return render(request,'books/book_list.html',{'books':books})

def book_create(request):
    return render(request,'books/book_create.html')

def book_store(request):
    if request.method=="POST":
        title=request.POST.get('title')
        author=request.POST.get('author')
        price=request.POST.get('price')
        publish_date=request.POST.get('publish_date') 
        errors={}
        if not title:
            errors['title']='Title is Required'
        if not author:
            errors['author']='Title is Required'
        if not price:
            errors['price']='Title is Required'
        if not publish_date:
            errors['publish_date']='Title is Required'

        if errors:
            return render(request, 'students/create.html', {
                'errors': errors,
                'old': request.POST 
            })
        Book.objects.create(title=title,author=author,price=price,published_date=publish_date)
        return redirect('book_list')

def book_edit(request,id):
    # book=book.objects.get(id=id)
    book=get_object_or_404(Book,id=id)
    return render(request,'books/book_edit.html',{'book':book})
def book_update(request,id):
    book=get_object_or_404(Book,id=id)
    if request.method=='POST':
        book.title=request.POST.get('title')
        book.author=request.POST.get('author')
        book.price=request.POST.get('price')
        book.published_date=request.POST.get('publish_date')
        book.save()
        return redirect('book_list')

def book_delete(request,id):
    book=get_object_or_404(Book,id=id)
    book.delete()
    return redirect('book_list')
