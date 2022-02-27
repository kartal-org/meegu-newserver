from urllib import request
from rest_framework import generics, permissions, status, response
from .models import *
from workspaces.models import *
from .serializers import *
from workspaces.serializers import FileSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from .permissions import *
from django.db.models import Q
from institutions.models import Member
from rest_framework import filters


class ResourceList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ResourceSerializer
    parser_classes = [MultiPartParser, FormParser]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "description", "institution__name"]

    def get_queryset(self):
        """
        Resource query Filters
        """
        user = self.request.user
        institution = self.request.query_params.get("institution")
        isArchive = self.request.query_params.get("isArchive")
        fileType = self.request.query_params.get("fileType")
        forStudent = self.request.query_params.get("forStudent")

        queryset = Resource.active.all()

        if institution is not None:
            queryset = queryset.filter(institution__id=institution)

        if fileType is not None:
            if fileType == "pdf":
                queryset = queryset.filter(~Q(pdf=""))
            if fileType == "template":
                queryset = queryset.filter(~Q(richText=""))

        if isArchive is not None:
            queryset = Resource.objects.filter(isActive=False)

        if forStudent:
            # What do we look for: resource list based on student's institution affliation
            # What do we have now: student info
            # How do we solve the problem:
            # 1: Get all membership of the student
            membership = Member.objects.filter(user=user)
            # 2. Get all the institution id of that membership
            institutionIDs = []
            for x in membership.all():
                print(x.id)
                institutionIDs.append(x.institution.id)
            # breakpoint()
            # 3. Filter resource based on that id list
            queryset = queryset.filter(institution__id__in=institutionIDs)

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

        data = {
            "name": resource.name,
            "workspace": workspace.id,
        }

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        if pdf != "":
            serializer.save(pdf=pdf)
        if richText != "":
            serializer.save(richText=richText)

        resource.imports = resource.imports + 1
        data = serializer.data
        return response.Response(data, status=status.HTTP_200_OK)
