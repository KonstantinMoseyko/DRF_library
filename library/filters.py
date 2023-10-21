from django_filters import rest_framework as filters

from .models import Author, Book


class AuthorFilter(filters.FilterSet):
    last_name = filters.CharFilter(lookup_expr="contains")

    class Meta:
        model = Author
        fields = ["last_name"]


class BookFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr="contains")

    class Meta:
        model = Book
        fields = ["title"]
