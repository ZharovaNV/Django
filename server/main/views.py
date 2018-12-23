from django.shortcuts import render


def main_view(request):
    return render(request, 'main/index.html')

def contacts_view(request):
    return render(request, 'main/contacts.html')



