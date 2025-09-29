from django.urls import path
from .views import SubjectListView, SubjectDetailView

urlpatterns = [
    path("api/", SubjectListView.as_view(), name="subject-list"),
    path("api/<slug:slug>/", SubjectDetailView.as_view(), name="subject-detail"),
]
