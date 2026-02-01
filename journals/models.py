from django.db import models
from django.utils.text import slugify
from datetime import timedelta
import math

class Journal(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    TAG_CHOICES = [
        ("technology", "Tech"),
        ("career", "Career"),
        ("productivity", "Productivity"),
        ("featured", "Featured"),
    ]

    DEPARTMENT_CHOICES = [
        ("CS", "BS CS"),
        ("SE", "BS SE"),
        ("AI", "BS AI"),
        ("DS", "BS Data Science"),
        ("CyberSecurity", "BS CyberSecurity"),
        ("BBA", "BBA"),
        ("Accounting", "BS Accounting"),
        ("Economics", "BS Economics"),
        ("Social Sciences", "BS Social Sciences"),
        ("English", "BS English"),
        ("Psychology", "BS Psychology"),
        ("Other", "Other"),
    ]

    BATCH_CHOICES = [
    ("2020-24", "2020-24"),
    ("2021-25", "2021-25"),
    ("2022-26", "2022-26"),
    ("2023-27", "2023-27"),
    ("2024-28", "2024-28"),
    ("2025-29", "2025-29"),
    ("2026-30", "2026-30"),
    ("2027-31", "2027-31"),
]

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)

    author = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    batch = models.CharField(max_length=50, blank=True, null=True,choices=BATCH_CHOICES)
    department = models.CharField(max_length=100, blank=True, null=True,choices=DEPARTMENT_CHOICES)

    excerpt = models.TextField()
    content = models.TextField()  

    read_time = models.PositiveIntegerField(blank=True, null=True)
    tags = models.CharField(max_length=200, choices=TAG_CHOICES, blank=True, null=True)

    likes = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    is_featured_homepage = models.BooleanField(default=False)

    # cover_image_url = models.CharField(max_length=300, blank=True, null=True)  # Google Drive or other links
    # ig_username = models.CharField(max_length=100, blank=True, null=True)
    # li_username = models.CharField(max_length=100, blank=True, null=True)
    

    def save(self, *args, **kwargs): 
        if not self.slug:      # Auto-slug on first save
            self.slug = slugify(self.title)

        # Auto-generate read time
        if self.content:
            words = len(self.content.split())
            self.read_time = math.ceil(words / 200)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    



# ==================================================================================
# Flow like a story

# React says: “Hey Django, give me a list of journals.”
# Django looks at database → returns a JSON list with only short info.
# React shows journal cards.
# User clicks → React says: “Hey Django, give me full detail of journal with slug abc.”
# Django finds it → returns JSON with full detail.
# React shows the detail page.