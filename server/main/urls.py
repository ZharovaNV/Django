from django.urls import path
from .views import (
    main_view, contacts_view
)

app_name="main"

urlpatterns = [
    path('', main_view, name="index"),
    path('contacts/', contacts_view, name="contacts"),
]
