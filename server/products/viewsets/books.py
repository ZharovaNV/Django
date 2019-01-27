from rest_framework.viewsets import ModelViewSet

from products.models import Book
from products.serializers import DefaultBookSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = DefaultBookSerializer