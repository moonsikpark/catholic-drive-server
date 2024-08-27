from django.db import models

from pgvector.django import VectorField
from pgvector.django.indexes import HnswIndex

class DriveFolder(models.Model):
    user = models.ForeignKey("account.User", on_delete=models.CASCADE)
    path = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}:{self.path}"

class DriveFile(models.Model):
    name = models.CharField(max_length=255)
    folder = models.ForeignKey("DriveFolder", on_delete=models.CASCADE)
    file = models.FileField(upload_to='files')
    
    class FileTypeEnum(models.TextChoices):
        IMAGE = 'image'
        DOCUMENT = 'document'
    
    file_type = models.CharField(
        max_length=10,
        choices=FileTypeEnum.choices,
        default=FileTypeEnum.DOCUMENT,
        db_index=True
    )

    # for document, document itself. for image, ocr result
    textual_data = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class DriveFileEmbeddings(models.Model):
    # for text, each sentence.
    # for image, each sentence of gpt description.

    file = models.ForeignKey("DriveFile", on_delete=models.CASCADE)
    text = models.TextField()
    embeddings = VectorField(dimensions=1536, null=True, blank=True)
    processed = models.BooleanField(default=False, db_index=True)

    class Meta:
        indexes = [
            HnswIndex(
                name="embedding_index",
                fields=["embeddings"],
                m=16,
                ef_construction=64,
                opclasses=["vector_cosine_ops"],
            ),
        ]

    def __str__(self):
        return self.text
