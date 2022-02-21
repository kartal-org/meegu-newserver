from rest_framework import generics, permissions
from .models import *
from .serializers import *
from .renderers import CustomRenderer


class WorkspaceList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # renderer_classes = [CustomRenderer]
    # queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer

    def get_queryset(self):
        """
        Workspace query Filters
        """
        # Default filter based on members
        user = self.request.user
        queryset = Workspace.activeWorkspaces.filter(
            members__in=[
                user.id,
            ]
        )

        # Filters workspace based on isOwner
        isOwner = self.request.query_params.get("isOwner")
        isAdviser = self.request.query_params.get("isAdviser")

        if isOwner is not None:
            if isOwner:
                queryset = queryset.filter(creator=user)
            else:
                queryset = queryset.exclude(creator=user)
        if isAdviser:
            queryset = Workspace.activeWorkspaces.filter(adviser=user)
        print(queryset)
        return queryset


class WorkspaceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer
    renderer_classes = [CustomRenderer]


class FileList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # queryset = File.objects.all()
    serializer_class = FileSerializer
    renderer_classes = [CustomRenderer]

    def get_queryset(self):
        queryset = File.active.all()

        # Params
        status = self.request.query_params.get("status")
        workspace = self.request.query_params.get("workspace")
        archive = self.request.query_params.get("archive")

        if status is not None:
            print('status here')
            queryset = queryset.filter(status=status)
        if workspace is not None:
            queryset = queryset.filter(workspace=workspace)
        if archive:
            queryset = File.objects.filter(isActive=False)

        return queryset


class FileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = File.objects.all()
    serializer_class = FileSerializer
    renderer_classes = [CustomRenderer]
