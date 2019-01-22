from django.urls import path

from products.views import BookJsonListView

app_name = 'rest_books'

urlpatterns = [
    path('', BookJsonListView.as_view(), name='catalog')
]
