import json
from django.shortcuts import (
    render, redirect,
    get_list_or_404, get_object_or_404
)
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, ListView, DetailView,
    UpdateView, DeleteView
)


from .models import Book
from .forms import BookForm


class BookCreateView(CreateView):
    model = Book
    fields = fields = ['sname', 'sauthor', 'category', 'image', 'nprice', 'ncnt', 'sshortdescr', 'sfulldescr', 'sagerestrict', 'sisbn', 'npagecnt']
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:index')


class BookUpdateView(UpdateView):
    model = Book
    fields = fields = ['sname', 'sauthor', 'category', 'image', 'nprice', 'ncnt', 'sshortdescr', 'sfulldescr', 'sagerestrict', 'sisbn', 'npagecnt']
    template_name = 'products/update.html'
    success_url = reverse_lazy('products:index')


def book_create_view(request):
    success_url = reverse_lazy('catalog:index')
    form = BookForm()
    
    if request.method == 'POST':
        form = BookForm(request.POST, files=request.FILES)
        
        if form.is_valid():
            form.save()
            
            return redirect(succes_url)

    return render(
        request,
        'products/create.html',
        {
            'form': form
        }
    )

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

