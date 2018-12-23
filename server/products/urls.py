from django.urls import path
from .views import (
    catalog_view, book_view
)

urlpatterns = [
    path('', catalog_view),
    path('<int:pk>/', book_view),
]
