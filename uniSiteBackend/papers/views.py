from rest_framework import generics
from .models import Subject
from .serializers import SubjectListSerializer, SubjectDetailSerializer


# List all subjects
class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectListSerializer


# One subject with grouped resources
class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectDetailSerializer
    lookup_field = "slug"
