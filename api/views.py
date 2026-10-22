from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from catalog.models import Book
from .serializers import BookSerializer


@api_view(["GET", "POST"])
def book_list_create(request):
    # READ all books
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    # CREATE a new book
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

    # READ one book
    if request.method == "GET":
        serializer = BookSerializer(book)
        return Response(serializer.data)

    # UPDATE a book
    if request.method == "PUT":
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE a book
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)