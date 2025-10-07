from django.db import models

class Journal(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    batch = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    read_time = models.CharField(max_length=50, blank=True, null=True)
    excerpt = models.TextField()
    content = models.TextField()  # Store blog content (Markdown/HTML)
    cover_image_url = models.CharField(max_length=300, blank=True, null=True)  # Google Drive or other links
    tags = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True)
    likes = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    ig_username = models.CharField(max_length=100, blank=True, null=True)
    li_username = models.CharField(max_length=100, blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title


# Flow like a story

# React says: “Hey Django, give me a list of journals.”
# Django looks at database → returns a JSON list with only short info.
# React shows journal cards.
# User clicks → React says: “Hey Django, give me full detail of journal with slug abc.”
# Django finds it → returns JSON with full detail.
# React shows the detail page.