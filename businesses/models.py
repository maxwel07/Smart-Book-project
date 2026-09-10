from django.db import models

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    description = models.TextField()
    image = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    review_count = models.PositiveIntegerField(default=0)
    opening_time = models.TimeField(blank=True, null=True)
    closing_time = models.TimeField(blank=True, null=True)


    def is_open(self):
        from datetime import datetime

        current_time = datetime.now().time()

        return self.opening_time <= current_time <= self.closing_time

    def __str__(self):
        return self.name
