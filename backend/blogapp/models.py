from django.db import models
from django.contrib.auth.models import User

class BlogModel(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blogs"
    )

    title = models.CharField(max_length=75)
    subtitle = models.CharField(max_length=150, blank=True)

    image = models.ImageField(
        upload_to="blog_images/",
        blank=True,
        null=True
    )

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.title