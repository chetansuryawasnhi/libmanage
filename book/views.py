from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,authentication
from django.contrib.auth.models import User
from .serializers import RegisterSerializer,BookSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404
from .models import Book


class RegisterView(APIView):
    def post(self,request):
        data=request.data
        serializer=RegisterSerializer(data=data)
        if serializer.is_valid():
            user=serializer.save()
            return Response({
                "message":"user created succsfuully",
                "status":True
            },status=status.HTTP_201_CREATED
        )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
class LoginView(APIView):
    def post(self,request):
        data=request.data
        username=data.get('username')
        password=data.get('password')
        
        user=User.objects.filter(username=username).first()
        if user and user.check_password(password):
            refresh=RefreshToken.for_user(user)
            return Response({
                "acces_toekn":str(refresh.access_token),
                "refresh_toekn":str(refresh)
                
            })
        return Response({"messsage":"Invalid credantials"}, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user=request.user
        serializer=RegisterSerializer(user)
        return Response(serializer.data)
        

class StudentBookListView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self,request):  
        queryset = Book.objects.all()
        serializer_class = BookSerializer(queryset,many=True)
        print(serializer_class.data)
        return Response(serializer_class.data)

class BookCreateView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookUpdateView(APIView):
    permission_classes=[IsAuthenticated]
    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data, partial=True)  # `partial=True` allows updating only specific fields
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDeleteView(APIView):
    permission_classes=[IsAuthenticated]
    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
def student_view(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, 'student.html', {'books': books})