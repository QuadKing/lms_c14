from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse
from templated_mail.mail import BaseEmailMessage
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import Author, Book
from .permissions import IsAdminOrReadOnly
from .serializers import AuthorSerializer, BookSerializer
from .pagination import DefaultPagination, SecondDefaultPagination
from .filters import AuthorFilter, BookFilter


# Create your views here.

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = AuthorFilter
    search_fields = ['first_name', 'last_name']
    permission_classes = [IsAdminOrReadOnly]


def send_mail_function(request):
    try:
        # Simple pattern send mail
        # message = EmailMessage("Library Message", "Your book order is now available", "allwell@gmail.com", ["ojo@gmail.com"])
        # message.attach_file("book/static/images/MOSTBEAUTIFULplace 1.jpg")
        # message.send()

        # HTML message pattern here
        # template is how we pass information inside our template
        message = BaseEmailMessage(
            context={"name": "Allwell"}, template_name='book/email.html'
        )

        message.send(['elishaallwell1759@gmail.com'])

    except BadHeaderError:
        pass
    return HttpResponse('Message Sent!')


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookSerializer
    pagination_class = SecondDefaultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = BookFilter
    search_fields = ['title', 'price']
    permission_classes = [IsAdminUser]

# class BookList(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#     def get_serializer_context(self):
#         return {"request": self.request}
#
#
# class BookDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class AuthorList(ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#
# class AuthorDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


# class AuthorView(APIView):
#     def get(self, request):
#         authors = Author.objects.all()
#         serializers = AuthorSerializer(authors, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = AuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("success", status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def list_authors(request):
#     if request.method == 'GET':
#         authors = Author.objects.all()
#         serializers = AuthorSerializer(authors, many=True)
#         return Response(serializers.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = AuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("success", status=status.HTTP_201_CREATED)


# class AuthorDetailView(APIView):
#     def get(self, request, pk):
#         author = get_object_or_404(Author, pk=pk)
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         author = get_object_or_404(Author, pk=pk)
#         serializer = AuthorSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("detail updated", status=status.HTTP_200_OK)
#
#     def delete(self, request, pk):
#         author = get_object_or_404(Author, pk=pk)
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE'])
# def author_detail(request, pk):
#     author = get_object_or_404(Author, pk=pk)
#     if request.method == 'GET':
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = AuthorSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response("detail updated", status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializers = BookSerializer(books, many=True, context={'request': request})
#         return Response(serializers.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
