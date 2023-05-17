from django.http import HttpResponse
from django.shortcuts import render
from . import models


# Create your views here.
def kk(request):
    return HttpResponse('Hello World!!!')


def view_book(request):
    book = models.Book.objects.all()
    return render(request, 'book.html', {'book: book'})

