from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    preview_image = models.ImageField()
    post_image = models.ImageField()
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    short_content = models.TextField(blank=True)
    category = models.CharField(max_length=50)
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.short_content:
            self.short_content = self.content[:200] + '...'  # Generate shortened content
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    post_id = models.CharField(max_length=500)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.author} - {self.content}"

