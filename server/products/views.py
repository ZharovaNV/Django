import json
from django.shortcuts import render

# Create your views here.

def catalog_view(request):
    with open('data.json', 'r') as file:
        context = json.load(file)

    return render(
        request, 
        'products/catalog.html',
        {
            'books': context.get('books') or []
        }
    )

def book_view(request, pk):
    with open('data.json', 'r') as file:
        context = json.load(file)

    books = context.get('books')

    return render(
        request, 
        'products/book.html',
        {
            'object': books[pk] if len(books) > pk else ''
        }
    )
