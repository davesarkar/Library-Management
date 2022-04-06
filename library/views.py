from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password

from library.models import Book,MyUser

# Create your views here.
def register(request):
    message=""

    if request.POST:
        username = request.POST['username']
        password = make_password(request.POST['password'])

        try:
            user = MyUser.objects.get(username=username)
        except Exception:
            user = None
        if user:
            message = 'Username already exists'
        else:
            user = MyUser.objects.create(
                username=username,
                password=password
            )
        user.first_name = request.POST['f_name']
        user.last_name = request.POST['l_name']
        user.email = request.POST['email']
        user.role = 'Admin'
        user.save()
        return redirect('admin_home')
    context = {'message':message}
    return render(request, 'library/register.html', context)

def login_view(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
    
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            if request.user.role != 'Admin':
                return redirect('student-home')
            return redirect('admin_home')
        else:
            return HttpResponse('Invalid Credentials')
    return render(request, 'library/login.html')

def logout_view(request):
    logout(request)
    return HttpResponse('Logged out Successfully!')

@login_required(login_url='login')
def home(request):
    if request.user.role != 'Admin':
        return HttpResponse('You are not allowed here !')
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'library/admin-home.html', context)

@login_required(login_url='login')
def addBook(request):
    if request.user.role != 'Admin':
        return HttpResponse('You are not allowed here !')
    if request.POST:
        name = request.POST['name']
        author = request.POST['author']

        book, created = Book.objects.get_or_create(
            name = name,
            author = author
        )
        return redirect('admin_home')
    context = {'page':'create'}
    return render(request, 'library/add-book.html', context)

@login_required(login_url='login')
def editBook(request, id):
    if request.user.role != 'Admin':
        return HttpResponse('You are not allowed here !')
    book = Book.objects.get(id=id)
    if request.POST:
        name = request.POST['name']
        author = request.POST['author']
        book.name = name
        book.author = author
        book.save()
        return redirect('admin_home')
    context = {'book':book, 'page':'edit'}
    return render(request, 'library/add-book.html', context)

@login_required(login_url='login')
def deleteBook(request, id):
    if request.user.role != 'Admin':
        return HttpResponse('You are not allowed here !')
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('admin_home')

@login_required(login_url='login')
def studentHome(request):
    books = Book.objects.all()
    context = {'books':books}
    return render(request, 'library/student-home.html', context)