from django.db import models

# Create your models here.

class BusinessRegistration(models.Model):
    business_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20, blank=True)
    description = models.TextField()
    contact_email = models.EmailField(max_length=100)


    def __str__(self):
        return self.business_name