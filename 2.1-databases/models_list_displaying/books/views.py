from django.shortcuts import render, redirect
from books.models import Book

def index(request):
    return redirect('books')

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books' : books}
    return render(request, template, context)

def book_view(request, pub_date):
    template = 'books/book.html'
    list_books = Book.objects.all().order_by('pub_date')
    books = list_books.filter(pub_date = pub_date)
    for n, book in enumerate(list_books):
        if str(book.pub_date) == pub_date:
            index = n
    prev_date = False
    next_date = False
    count = list_books.count()
    if count > 1:
        n = index
        while str(list_books[n].pub_date) == pub_date and n > 1:
            n -= 1
        prev_date = list_books[n].pub_date if str(list_books[0].pub_date) != pub_date else False
        n = index
        while str(list_books[n].pub_date) == pub_date and n < count - 1:
            n += 1
        next_date = list_books[n].pub_date if str(list_books[count - 1].pub_date) != pub_date else False
    context = {
        'books' : books,
        'prev_date' : prev_date,
        'next_date' : next_date
        }
    return render(request, template, context)