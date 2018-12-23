from django.urls import path
from .views import (
    catalog_view, book_view
)

app_name="products"

urlpatterns = [
    path('', catalog_view, name="index"),
    path('<int:pk>/', book_view, name="book"),
]
