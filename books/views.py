from django.shortcuts import render
from django.views import generic
from django.urls import reverse,reverse_lazy


from .models import Book
class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
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

class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')

