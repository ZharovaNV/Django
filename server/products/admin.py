from django.contrib import admin
from django.template.loader import render_to_string
from .models import Book, Category

class BookAdmin(admin.ModelAdmin):
    list_display = [
        'sname', 'sauthor', 'picture', 'nprice', 'modified', 'created'
    ]

    def picture(self, obj):
        return render_to_string(
            'products/components/picture.html',
            {'url': obj.image.url }
        )



admin.site.register(Book, BookAdmin)
admin.site.register(Category)
