from rest_framework import generics, permissions
from .models import *
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import filters
from .permissions import *


class ArticleList(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated, IsStorageAllowed]
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = ArticleSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "title",
        "abstract",
    ]

    def get_queryset(self):
        queryset = Article.objects.all()

        status = self.request.query_params.get("status")
        institution = self.request.query_params.get("institution")
        department = self.request.query_params.get("department")

        if status is not None:
            queryset = queryset.filter(status=status)
        if institution is not None:
            queryset = queryset.filter(institution__id=institution)
        if department is not None:
            queryset = queryset.filter(department__id=department)

        return queryset


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ReviewList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        queryset = Review.objects.all()

        article = self.request.query_params.get("article")
        rate = self.request.query_params.get("rate")

        if article is not None:
            queryset = queryset.filter(article__id=article)
        if rate is not None:
            queryset = queryset.filter(rate=rate)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
