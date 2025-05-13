from django.shortcuts import render
from django.http import JsonResponse

def api_home(request):
    # For API clients
    if request.headers.get('Content-Type') == 'application/json':
        return JsonResponse({
            'message': 'Welcome to the Book Catalog API',
            'endpoints': {
                'list/create books': '/api/books/',
                'retrieve/update/delete book': '/api/books/<id>/',
                'admin interface': '/admin/'
            }
        })
    # For web browsers
    return render(request, 'books/home.html')

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer