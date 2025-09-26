from django.shortcuts import render
from django.http import JsonResponse
from .models import Book

# Create your views here.


def book_list(request):
    books=list(Book.objects.values())
    return JsonResponse(books, safe=False)