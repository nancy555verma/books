from rest_framework import serializers, mixins
from .models import Book
from django.contrib.auth.models import User


class ReadUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name")
        read_only_fields = fields


class WriteBookSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")
    # updated_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")

    # user = ReadUserSerializer()

    class Meta:
        model = Book
        fields = ("id", "title", "author", "user", "is_read", "created_at", "updated_at")


class ReadBookSerializer(serializers.ModelSerializer):
    user = ReadUserSerializer()
    # created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")
    # updated_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")

    class Meta:
        model = Book
        fields = ("id", "title", "author", "user", "is_read", "created_at", "updated_at")

        read_only_fields = fields


class MarkBookSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")
    # updated_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")

    class Meta:
        model = Book
        fields = ("id", "title", "author", "user", "is_read", "created_at", "updated_at")

