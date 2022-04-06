from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from library.models import Book

# Create your views here.
def register(request):
    return

def login_view(request):
    return render(request, 'library/login.html')

def logout_view(request):
    return render(request, 'library/login.html')

def home(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'library/admin-home.html', context)

def addBook(request):
    if request.POST:
        name = request.POST['name']
        author = request.POST['author']

        book, created = Book.objects.get_or_create(
            name = name,
            author = author
        )
        return redirect('admin_home')

    return render(request, 'library/add-book.html')

def editBook(request):
    return render(request, 'library/add-book.html')

def deleteBook(request):
    return 

def studentHome(request):
    return render(request, 'library/student-home.html')