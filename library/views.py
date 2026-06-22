from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status 
from rest_framework.authentication import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import *


@api_view(["POST"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def book_add(request):
    serializers =  BookAddUpdateDeleteSerializers(data=request.data)
    serializers.is_valid(raise_exception=True)
    serializers.save()
    return Response({"message": "book add successfully!"}, status=status.HTTP_201_CREATED)


@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def book_update(request, id):
    book = get_object_or_404(Book, id=id, author=request.user)
    serializers = BookAddUpdateDeleteSerializers(book, data=request.data, partial=True)
    serializers.is_valid(raise_exception=True)
    serializers.save()
    return Response({"message": "book update successfully"}, status=status.HTTP_200_OK)
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def search_book(request):
    book = Book.objects.filter(author=request.user)
    serializers = BookAddUpdateDeleteSerializers(book, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)

    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def search_all_book(request):
    all_book = Book.objects.all().order_by()
    serializers = BookAddUpdateDeleteSerializers(all_book, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def search(request, title):
    books = Book.objects.filter(title__icontains=title)
    if not books.exists():
        return Response(
            {"message": "No books found with that title."},
            status=status.HTTP_404_NOT_FOUND
        )
    serializers = BookAddUpdateDeleteSerializers(books, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)



@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id, author=request.user)
    book.delete()
    return Response({"message": "book delete successfully!"}, status=status.HTTP_200_OK)
