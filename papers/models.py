from django.db import models
from django.utils.text import slugify

class Subject(models.Model):
    subject_title = models.CharField(max_length=260)
    slug = models.SlugField(unique=True, max_length=255)
    # description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.subject_title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.subject_title


class Resource(models.Model):
    RESOURCE_TYPES = [
        ("past_paper", "Past Paper"),
        ("quiz", "Quiz"),
        ("assignment", "Assignment"),
        ("book", "Book"),
        ("notes", "Notes"),
        ("other", "Other"),
    ]

    subject = models.ForeignKey(
        Subject, related_name="resources", on_delete=models.CASCADE
    )
    resource_name = models.CharField(max_length=260)
    resource_link = models.CharField(max_length=260)
    type = models.CharField(max_length=20, choices=RESOURCE_TYPES)


    # "resource_name": "2021 - Sessional 1",
    # "resource_link": "https://drive.google.com/file/d/abc123/view"

    def __str__(self):
        return f"{self.subject.subject_title} - {self.resource_name} ({self.type})"
