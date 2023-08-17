from django.db import models
from agents.models import Agents

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='property_images/')
    house_address = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    amount = models.IntegerField()
    status = models.TextField()
    beds = models.IntegerField()
    baths = models.IntegerField()
    garages = models.IntegerField()
    area = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    agent = models.ForeignKey(Agents, on_delete=models.SET_NULL, null=True)


    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'properties'

    def __str__(self):
        return self.name


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='property_images')
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return self.property.name


class Amenity(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='amenity')
    amenity = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Amenities'

    def __str__(self):
        return self.amenity

