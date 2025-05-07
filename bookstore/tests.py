from django.test import TestCase
from .models import Book
from .serializers import BookSerializer

class BookSerializerTestCase(TestCase):
    def test_book_serializer(self):
        book = Book.objects.create(title="Test Book", author="Test Author", price=19.99, description="A test book description")
        serializer = BookSerializer(book)
        self.assertEqual(serializer.data['price'], '19.99')