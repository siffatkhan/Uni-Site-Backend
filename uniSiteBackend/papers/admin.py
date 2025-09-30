from django.contrib import admin
from .models import Subject,Resource

# Register your models here.
# admin.site.register(Subject)
# admin.site.register(Resource)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=("subject_title","slug")
    prepopulated_fields={"slug":("subject_title",)}


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display=("resource_name","type","subject")
    list_filter=("type","subject")
    search_fields=("resource_name", "resource_link")