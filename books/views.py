from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import DeleteView
from books.models import Book, Author, Publisher


class BooksModelView(TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model.list'] = ['Book', 'Author', 'Publisher']
        return context


class BookList(ListView):
    model = Book


class AuthorList(ListView):
    model = Author


class PublisherList(ListView):
    model = Publisher


class BookDetail(DeleteView):
    model = Book


class AuthorDetail(DeleteView):
    model = Author


class Publisher(DeleteView):
    model = Publisher
