from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relacionamento com o usuário
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # Relacionamento com o livro
    quantity = models.PositiveIntegerField(default=1)  # Quantidade de livros
    total_price = models.DecimalField(max_digits=7, decimal_places=2)  # Preço total da compra
    ordered_at = models.DateTimeField(auto_now_add=True)  # Data de criação do pedido

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
