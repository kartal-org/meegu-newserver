from rest_framework import generics, permissions, status, response
from .models import *
from .serializers import *


class RecommendationList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

    def get_queryset(self):
        """
        Recommendation query Filters
        """
        # Default filter based on ownership
        user = self.request.user
        archive = self.request.query_params.get("archive")
        workspace = self.request.query_params.get("workspace")
        institution = self.request.query_params.get("institution")
        status = self.request.query_params.get("status")
        queryset = Recommendation.active.all()

        if workspace is not None:
            queryset = queryset.filter(file__workspace__id=workspace)
        if status is not None:
            queryset = queryset.filter(status=status)
        if institution is not None:
            queryset = queryset.filter(institution__id=institution)

        if archive:
            queryset = Recommendation.objects.filter(isActive=False)

        return queryset


class RecommendationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class CommentList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        """
        Comment query Filters
        """

        archive = self.request.query_params.get("archive")
        file = self.request.query_params.get("file")
        queryset = Comment.active.all()

        if file is not None:
            queryset = queryset.filter(file__id=file)

        if archive:
            queryset = Comment.objects.filter(isActive=False)

        return queryset


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return response.Response(serializer.data, status=status.HTTP_200_OK)


class ReplyList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReplySerializer

    def get_queryset(self):
        """
        Reply query Filters
        """

        archive = self.request.query_params.get("archive")

        queryset = Reply.active.all()

        if archive:
            queryset = Reply.objects.filter(isActive=False)

        return queryset


class ReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
