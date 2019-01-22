from django.views.generic import (
    ListView, DetailView
)
from django.urls import reverse_lazy
from django.http import JsonResponse

from products.models import Category

class CategoryJsonListView(ListView):
    model = Category

    def get_context_data(self, **kwargs):
        query = self.model.objects.all()

        return {
            'results': list(
                map(
                    lambda itm: {
                        'id': itm.id,
                        'sname': itm.sname,
                    },
                    query
                )
            )
        }

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class CategoryListView(ListView):
    model = Category
    template_name = 'categories/list.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/detail.html'

    def get_context_data(self, **kwargs):
        obj = kwargs.get('object')
        books = obj.book_set.all()

        return {
            'object': obj,
            'books': books
        }


   