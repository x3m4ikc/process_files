from rest_framework import generics

from .models import File
from .serializers import FileSerializer
from .tasks import process_file


class FileUploadView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def processing_create(self, serializer):
        instance = serializer.save()
        process_file.delay(instance.id)


class FileListView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
