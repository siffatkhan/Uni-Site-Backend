from rest_framework import generics, status 
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from .models import Journal
from .serializers import JournalListSerializer, JournalDetailSerializer

# List view (for all journals)
class JournalListView(generics.ListAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalListSerializer

# Detail view (for one journal by slug)
class JournalDetailView(generics.RetrieveAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalDetailSerializer
    lookup_field = 'slug'

class FeaturedJournalView(RetrieveAPIView):
    serializer_class = JournalDetailSerializer

    def get_object(self):
        # Return the first featured journal
        return Journal.objects.filter(is_featured=True).first()

    def get(self, request, *args, **kwargs):
        journal = self.get_object()
        if not journal:
            return Response({"detail": "No featured journal found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(journal)
        return Response(serializer.data)
