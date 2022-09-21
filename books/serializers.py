
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from books.models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
