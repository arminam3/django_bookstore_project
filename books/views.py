from django.shortcuts import render
from django.views import generic

from .models import Book
class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookDetailsView(generic.DetailView):
    model = Book
    template_name = 'books/book_details.html'

class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = '__all__'

class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    fields = '__all__'


