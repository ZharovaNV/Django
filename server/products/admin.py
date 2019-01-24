from datetime import datetime
from django.contrib import admin
from django.template.loader import render_to_string
from .models import Book, Category

class BookAdmin(admin.ModelAdmin):
    list_display = [
        'sname', 'sauthor', 'category', 'picture', 'nprice', 'modified', 'created', 'is_new'
    ]
    list_filter = [
        'category', 'image','modified', 'created'
    ]
    search_fields = [
        'sname', 'sauthor'
    ]
    fieldsets = (
        (
            'Main', {
                'fields': ('sname', 'sauthor')
            }
        ),
        (
            'Others', {
                'fields': ('category','image','nprice',
                'ncnt','sshortdescr','sfulldescr','sagerestrict',
                'sisbn','npagecnt')
            }
        )
    )

    def picture(self, obj):
        return render_to_string(
            'products/components/picture.html',
            {'url': obj.image.url }
        )

    def is_new(self, obj):
        return datetime.now().date() == obj.created.date()




admin.site.register(Book, BookAdmin)
admin.site.register(Category)
