from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.views import View
from .models import Book

from rest_framework import viewsets
from .serializers import BookSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

def first(request):
    books = Book.objects.all()
    return render(request, 'first.html', {'books': books})

# class Another(View):

#     book = Book.objects.get(id=1)
#     output = f"we have {book.title} book with ID {book.id}<br>"
#     def get(self, request):
#         return HttpResponse(self.output)

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)