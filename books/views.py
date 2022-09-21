from os import stat
from django.shortcuts import render


from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from books.models import Book
from books.serializers import BookSerializer

# Create your views here.


class Login(APIView):
    
    def post(self, request):
        user = authenticate(username=request.data.get(
            "username"), password=request.data.get("password"))
        if not user:
            return Response({'error': 'Credentials are incorrect or user does not exist'}, status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=HTTP_200_OK)



class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]







def index(request):
    return render(request, 'books/index.html')
