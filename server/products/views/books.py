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


from products.models import Book
from products.forms import BookForm

from django.core.paginator import Paginator
from django.http import JsonResponse


class BookJsonListView(ListView):
    model = Book
    # context_object_name = 'books'
    # template_name = 'products/catalog.html'
    paginate_by = 3

    def serialize_object_list(self, queryset):
        return list(
                map(
                    lambda itm: {
                        'id': itm.id,
                        'sname': itm.sname,
                        'sauthor': itm.sauthor,
                        'category': itm.category.sname,
                        'image': itm.image.url,
                        'nprice': itm.nprice,
                        'ncnt': itm.ncnt,
                        'sshortdescr': itm.sshortdescr,
                        'sfulldescr': itm.sfulldescr,
                        'sagerestrict': itm.sagerestrict,
                        'sisbn': itm.sisbn,
                        'npagecnt': itm.npagecnt,
                    },
                    queryset
                )
            )

    def get_context_data(self, **kwargs):
        context = super(BookJsonListView, self).get_context_data(**kwargs)

        data = {}
        page = context.get('page_obj')
        route_url = reverse_lazy('rest_books:catalog')

        data['next_url'] = None
        data['previous_url'] = None
        data['page'] = page.number
        data['count'] = page.paginator.count
        data['results'] = self.serialize_object_list(page.object_list)

        if page.has_next():
            data['next_url'] = f'{route_url}?page={page.next_page_number}'

        if page.has_previous():
            data['previous_url'] = f'{route_url}?page={page.previous_page_number}'

        return data

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)

class BookCreateView(CreateView):
    model = Book
    fields = ['sname', 'sauthor', 'category', 'image', 'nprice', 'ncnt', 'sshortdescr', 'sfulldescr', 'sagerestrict', 'sisbn', 'npagecnt']
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:index')


class BookUpdateView(UpdateView):
    model = Book
    fields = fields = ['sname', 'sauthor', 'category', 'image', 'nprice', 'ncnt', 'sshortdescr', 'sfulldescr', 'sagerestrict', 'sisbn', 'npagecnt']
    template_name = 'products/update.html'
    success_url = reverse_lazy('products:index')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products:index')


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'products/catalog.html'
    paginate_by = 3


class BookDetailView(DetailView):
    model = Book
    template_name = 'products/book.html'



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

