from django.db import models

# Create your models here.
class Agents(models.Model):
    name = models.CharField(max_length=100)
    agent_pic = models.ImageField(upload_to='agent_pics')
    bio = models.TextField(blank=False)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name
