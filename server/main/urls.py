from django.urls import path
from .views import (
    main_view, contacts_view
)

urlpatterns = [
    path('', main_view),
    path('contacts/', contacts_view),
]
