from rest_framework import serializers
from .models import Subject, Resource


class SubjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["subject_title", "slug"]


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ["resource_name", "resource_link", "type"]


class SubjectDetailSerializer(serializers.ModelSerializer):
    resources = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        fields = ["subject_title", "slug", "resources"]

    def get_resources(self, obj):
        grouped = {key: [] for key, _ in Resource.RESOURCE_TYPES}
        for resource in obj.resources.all():
            grouped[resource.type].append(
                {
                    "resource_name": resource.resource_name,
                    "resource_link": resource.resource_link,
                }
            )
        return grouped


# serializers.ModelSerializer → DRF’s shortcut class. It auto-generates fields from the model.

# Meta → configuration class.
# model = Subject → we’re serializing the Subject model.
# fields = [...] → only include these three fields in the JSON response.