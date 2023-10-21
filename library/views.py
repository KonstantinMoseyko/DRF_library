from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

from .filters import AuthorFilter, BookFilter
from .models import Author, Book
from .serializers import AuthorModelSerializer, BookModelSerializer


class AuthorPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20


class BookPageNumberPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20


class AuthorModelViewSet(ModelViewSet):
    pagination_class = AuthorPageNumberPagination
    filterset_class = AuthorFilter
    serializer_class = AuthorModelSerializer
    queryset = Author.objects.all()

    @action(detail=True, methods=['get'])
    def get_author_name(self, request, pk):
        author = get_object_or_404(Author, pk=pk)
        return Response({'name': str(author)})


class BookModelViewSet(ModelViewSet):
    pagination_class = BookPageNumberPagination
    filterset_class = BookFilter
    serializer_class = BookModelSerializer
    queryset = Book.objects.all()
