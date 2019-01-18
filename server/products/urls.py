from django.urls import path
from .views import (
    catalog_view, book_view,
    book_create_view,
    BookCreateView, BookUpdateView
)

app_name="products"

urlpatterns = [
    path('create/', BookCreateView.as_view(), name="create"),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='update'),
    path('', catalog_view, name="index"),
    path('<int:pk>/', book_view, name="book"),
]
