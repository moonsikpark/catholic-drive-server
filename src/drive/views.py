from django.shortcuts import render

from rest_framework import viewsets
from django.http import Http404

# Create your views here.
from .models import DriveFolder, DriveFile, DriveFileEmbeddings

from .serializers import DriveFolderSerializer

class DriveFolderViewSet(viewsets.ModelViewSet):
    queryset = DriveFolder.objects.all()
    serializer_class = DriveFolderSerializer

    def list(self, request, *args, **kwargs):
        path = request.query_params.get('path')
        if path:
            try:
                self.queryset = self.queryset.filter(parent=self.queryset.get(path=path)) | self.queryset.filter(path=path)
            except DriveFolder.DoesNotExist:
                raise Http404("Folder does not exist")
            return super().list(request, *args, **kwargs)
        raise Http404("Path not provided")