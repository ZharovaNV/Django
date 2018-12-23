import json
from django.shortcuts import (
    render, get_list_or_404, get_object_or_404
)

from .models import Book

def catalog_view(request):
    # with open('data.json', 'r') as file:
    #     context = json.load(file)

    # return render(
    #     request, 
    #     'products/catalog.html',
    #     {
    #         'books': context.get('books') or []
    #     }
    # )
    return render(
        request,
        'products/catalog.html',
        {
            'books': get_list_or_404(Book)
        }
    )

def book_view(request, pk):
    # with open('data.json', 'r') as file:
    #     context = json.load(file)

    # books = context.get('books')

    # return render(
    #     request, 
    #     'products/book.html',
    #     {
    #         'object': books[pk] if len(books) > pk else ''
    #     }
    # )
    return render(
        request,
        'products/book.html',
        {
            'object': get_object_or_404(Book, id=pk)
        }
    )

