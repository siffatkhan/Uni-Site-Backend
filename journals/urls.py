from django.urls import path
from .views import JournalListView, JournalDetailView, FeaturedJournalView

urlpatterns = [
    path("api/", JournalListView.as_view(), name="journal_list"),
    path("api/featured/",FeaturedJournalView.as_view(), name="featured_journal"),
    path("api/<slug:slug>/",JournalDetailView.as_view(),name="journal_detail"),
]
