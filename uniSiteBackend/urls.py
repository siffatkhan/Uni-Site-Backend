
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/api/', views.contact_view, name="contact" ),
    path('books/', include("books.urls")),
    path('journals/', include('journals.urls')),
    path('papers/', include('papers.urls')),
]
