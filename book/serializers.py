from decimal import Decimal

from rest_framework import serializers
from .models import Author, Book
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as CurrentUserSerializer


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['title', 'author', 'book_number', 'description', 'date_added', 'genre', 'language',
                  'price', 'discount_price']

    author = serializers.HyperlinkedRelatedField(
        queryset=Author.objects.all(),
        view_name='author-detail'
    )
    book_number = serializers.CharField(max_length=10, source='isbn')
    discount_price = serializers.SerializerMethodField(method_name='calculate')

    def calculate(self, book: Book):
        return book.price * Decimal(0.5)


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
