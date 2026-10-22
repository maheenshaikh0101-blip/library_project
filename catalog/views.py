from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .models import Book


def home(request):
    books = Book.objects.all()
    context = {
        "total_books": books.count(),
        "total_genres": books.values("genre").distinct().count(),
        "total_members": User.objects.count(),
        "latest_books": books.order_by("-id")[:4],
    }
    return render(request, "catalog/home.html", context)


def about(request):
    return render(request, "catalog/about.html")


def book_list(request):
    query = request.GET.get("q", "").strip()
    selected_genre = request.GET.get("genre", "").strip()

    books = Book.objects.all().order_by("-id")
    if query:
        books = books.filter(Q(title__icontains=query) | Q(author__icontains=query))
    if selected_genre:
        books = books.filter(genre=selected_genre)

    genres = Book.objects.values_list("genre", flat=True).distinct().order_by("genre")
    return render(request, "catalog/book_list.html", {
        "books": books,
        "genres": genres,
        "query": query,
        "selected_genre": selected_genre,
    })


def book_create(request):
    if request.method == "POST":
        Book.objects.create(
            title=request.POST["title"],
            author=request.POST["author"],
            genre=request.POST["genre"],
        )
        messages.success(request, "Book added successfully!")
        return redirect("book_list")

    return render(request, "catalog/book_form.html")


def book_update(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.title = request.POST["title"]
        book.author = request.POST["author"]
        book.genre = request.POST["genre"]
        book.save()
        messages.success(request, "Book updated successfully!")
        return redirect("book_list")

    return render(request, "catalog/book_update.html", {"book": book})


def book_delete(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted.")
        return redirect("book_list")

    return render(request, "catalog/book_delete.html", {"book": book})
