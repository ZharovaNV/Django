from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['sname', 'sauthor', 'category', 'image', 'nprice', 'ncnt', 'sshortdescr', 'sfulldescr', 'sagerestrict', 'sisbn', 'npagecnt']