from django.urls import path
from products.views import (
    catalog_view, book_view,
    book_create_view,
    BookCreateView, BookUpdateView, BookDeleteView,
    BookListView, BookDetailView
)

app_name="products"

urlpatterns = [
    path('create/', BookCreateView.as_view(), name="create"),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='delete'),
    path('', BookListView.as_view(), name="index"),
    path('<int:pk>/', BookDetailView.as_view(), name="book"),
]
