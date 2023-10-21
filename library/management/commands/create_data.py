from library.models import Book, Author
from django.core.management.base import BaseCommand

AUTHORS_AMOUNT = 20

class Command(BaseCommand):

    def handle(self, *args, **options):
        for author_num in range(1, AUTHORS_AMOUNT+1):
            print(author_num)

            author = Author.objects.create(
                first_name=f'Имя автора {author_num}',
                last_name=f'Фамилия автора {author_num}',
                birthday_year=1999,
            )
            
            book = Book.objects.create(
                title=f'Название книги {author_num}',
            )
            book.authors.add(author)
