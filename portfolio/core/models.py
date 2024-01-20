from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
def custom_upload_to(instance, filename):
    old_instance = About.objects.get(pk=instance.pk)
    old_instance.image.delete()
    return 'about/' + filename

def custom_portfolio_upload_to(instance, filename):
    pass


class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    birthday = models.DateField()
    phone = PhoneNumberField()
    email = models.EmailField()
    image = models.ImageField(null=True, blank=True, upload_to=custom_upload_to)


class Education(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    
class Experience(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    images = models.ImageField(null=True, blank=True, upload_to="portfolio")
    link = models.URLField(blank=True, null=True)