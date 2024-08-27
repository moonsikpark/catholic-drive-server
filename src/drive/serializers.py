from rest_framework.serializers import ModelSerializer

from .models import DriveFolder, DriveFile, DriveFileEmbeddings

class DriveFolderSerializer(ModelSerializer):
    class Meta:
        model = DriveFolder
        fields = '__all__'