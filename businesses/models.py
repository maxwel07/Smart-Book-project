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

    class Meta:
            verbose_name = "Business"
            verbose_name_plural = "Businesses"

    def is_open(self):
        from datetime import datetime

        if not self.opening_time or not self.closing_time:
            return False

        current_time = datetime.now().time()

        return self.opening_time <= current_time <= self.closing_time

    def __str__(self):
        return self.name


    
class BusinessImage(models.Model):
    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.URLField()
    image_type = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Business Image"
        verbose_name_plural = "Business Images"

    def __str__(self):
        return f"{self.business.name} - {self.image_type}"


class Service(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='services')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    duration = models.PositiveIntegerField(help_text='Duration in minutes')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.business.name} - {self.name}'


class Reviews(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='reviews')
    customer_name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return f'{self.customer_name} - {self.business.name}'

