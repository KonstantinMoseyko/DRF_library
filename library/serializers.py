from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import Author, Book


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
    

class BookModelSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'
