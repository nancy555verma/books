from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import WriteBookSerializer, ReadBookSerializer, MarkBookSerializer


# Create your views here.


class BookModelViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ('title', 'author')
    ordering_fields = ('created_date', 'updated_date')
    filterset_fields = ('title', 'author')
    # serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadBookSerializer
        return WriteBookSerializer


class MarkBookModelViewSet(GenericAPIView, UpdateModelMixin):
    permission_classes = (IsAuthenticated,)
    # queryset = Book.objects.all()
    serializer_class = MarkBookSerializer

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
