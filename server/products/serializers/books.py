from rest_framework.serializers import (
    ModelSerializer, SerializerMethodField
)

from products.models import Book

class DefaultBookSerializer(ModelSerializer):
    category = SerializerMethodField()
    image = SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            'id','sname','sauthor','category','image','nprice',
            'ncnt','sshortdescr','sfulldescr','sagerestrict',
            'sisbn','npagecnt',
        ]

    def get_category(self, obj):
        return obj.category.sname

    def get_image(self, obj):
        return obj.image.url