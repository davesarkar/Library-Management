from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from library.models import Book,MyUser
from .serializers import BookSerializer
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['GET'])
def getRoutes(request):
    return Response([
        {'method':'POST', 'url':'api/token/'},
        {'method':'POST', 'url':'api/token/refresh'},
        {'method':'GET', 'url':'api/view-books'},
        {'method':'GET', 'url':'api/view-book'},
        {'method':'POST', 'url':'api/add-book'},
        {'method':'PUT', 'url':'api/edit-book/{id}'},
        {'method':'Delete', 'url': 'api/delete-book/{id}'},
    ])

@api_view(['POST'])
def register(request):
    data = request.data
    username = data['username']
    password = make_password(data['password'])
    role = data['role']

    try:
        user = MyUser.objects.create(
            username = username,
            password = password,
        )
        user.role = role
        user.save()
        refresh = RefreshToken.for_user(user)

        res = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    except Exception:
        res = {'message': 'username already exists'}

    return Response(res)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def viewBooks(request):
    books = Book.objects.all()
    serial = BookSerializer(books, many=True)
    return Response(serial.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def viewBook(request, id):
    book = Book.objects.get(id=id)
    serial = BookSerializer(book)
    return Response(serial.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addBook(request):
    if request.user.role == 'Student':
        return Response({'message':"You don't have permission to do this"})
    data = request.data
    book, created = Book.objects.get_or_create(name=data['name'], author=data['author'])
    return Response({"message":"Book created successfully !"})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def editBook(request,id):
    if request.user.role == 'Student':
        return Response({'message':"You don't have permission to do this"})
    data = request.data
    book = Book.objects.get(id=id)
    book.name = data['name']
    book.author = data['author']
    book.save()
    return Response({'message':"Book edited successfully !"})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteBook(request, id):
    if request.user.role == 'Student':
        return Response({'message':"You don't have permission to do this"})
    book = Book.objects.get(id=id)
    book.delete()
    return Response({'message':"Book deleted successfully !"})
