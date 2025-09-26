from . import views
from django.urls import path

urlpatterns =[
    path("api/books/",views.book_list, name="book_list"),
]