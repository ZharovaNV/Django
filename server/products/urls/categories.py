from django.urls import path
from products.views import (
    CategoryListView, CategoryDetailView
)


app_name = "categories"


urlpatterns = [
    path('<int:pk>/', CategoryDetailView.as_view(), name="detail"),
    path('', CategoryListView.as_view(), name="index"),
]
