from rest_framework import generics, permissions, status, response
from .models import *
from workspaces.models import *
from .serializers import *
from workspaces.serializers import FileSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from .permissions import *
from django.db.models import Q


class ResourceList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsStorageAllowed]
    serializer_class = ResourceSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        """
        Resource query Filters
        """

        institution = self.request.query_params.get('institution')
        isActive = self.request.query_params.get('isActive')
        fileType = self.request.query_params.get('fileType')

        queryset = Resource.active.all()

        if institution is not None:
            queryset = queryset.filter(institution=institution)

        if fileType is not None:
            if fileType == "pdf":
                queryset = queryset.filter(~Q(pdf=""))
            if fileType == "template":
                queryset = queryset.filter(~Q(richText=""))

        if isActive is not None:
            queryset = Resource.objects.filter(isActive=isActive)

        return queryset


class ResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class ImportResource(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FileSerializer

    def post(self, request):
        resource = Resource.objects.get(id=request.data.get("resource"))
        workspace = Workspace.objects.get(id=request.data.get("workspace"))

        pdf = resource.pdf
        richText = resource.richText

        data = {"name": resource.name, "workspace": workspace.id, }

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        if pdf != "":
            serializer.save(pdf=pdf)
        if richText != "":
            serializer.save(richText=richText)

        resource.imports = resource.imports + 1
        data = serializer.data
        return response.Response(data, status=status.HTTP_200_OK)
