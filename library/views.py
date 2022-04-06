from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def register(request):
    return

def login_view(request):
    return render(request, 'library/login.html')

def logout_view(request):
    return render(request, 'library/login.html')

def home(request):
    return render(request, 'library/admin-home.html')

def addBook(request):
    return render(request, 'library/add-book.html')

def editBook(request):
    return render(request, 'library/add-book.html')

def deleteBook(request):
    return 

def studentHome(request):
    return render(request, 'library/student-home.html')