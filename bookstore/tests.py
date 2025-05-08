from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookSerializerTestCase(TestCase):
    def test_book_serializer(self):
        book = Book.objects.create(title="Test Book", author="Test Author", price=19.99, description="A test book description")
        serializer = BookSerializer(book)
        self.assertEqual(serializer.data['price'], '19.99')

class BookViewSetTestCase(APITestCase):
    def test_create_book(self):
        data = {
            'title': 'Novo Livro',
            'author': 'Autor Exemplo',
            'description': 'Descrição do livro',
            'price': '29.90'
        }
        response = self.client.post('/api/books/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Novo Livro')
