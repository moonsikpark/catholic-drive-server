from django.contrib import admin
from .models import DriveFolder, DriveFile, DriveFileEmbeddings

class DriveFileInline(admin.TabularInline):
    model = DriveFile
    extra = 0

class DriveFolderInline(admin.TabularInline):
    model = DriveFolder
    extra = 0

class DriveFileEmbeddingsInline(admin.TabularInline):
    model = DriveFileEmbeddings
    extra = 0

# Register your models here.
@admin.register(DriveFolder)
class DriveFolderAdmin(admin.ModelAdmin):
    inlines = [DriveFolderInline, DriveFileInline]
    list_display = ['user', 'path', 'parent__path']
    search_fields = ['user__username', 'path', 'parent_folder__path']

@admin.register(DriveFile)
class DriveFileAdmin(admin.ModelAdmin):
    inlines = [DriveFileEmbeddingsInline]
    list_display = ['name', 'folder', 'file_type']
    search_fields = ['name', 'folder__path']
