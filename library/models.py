from uuid import uuid4
from django.db import models


class Author(models.Model):
    """Модель авторов"""
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['id']
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'first_name',
                    'last_name',
                ],
                name='unique_authors'
            )
        ]

    uuid = models.UUIDField(default=uuid4)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.birthday_year})'


class Book(models.Model):
    """Модель книжек"""
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['id']

    uuid = models.UUIDField(default=uuid4)
    title = models.CharField(max_length=64, unique=True)
    authors = models.ManyToManyField(Author)
