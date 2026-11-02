from django.contrib import admin
from . import models

admin.site.register(models.Business)
admin.site.register(models.BusinessImage)
admin.site.register(models.Service)
admin.site.register(models.Reviews)

@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'customer',
        'business',
        'service',
        'appointment_date',
        'start_time',
        'status',
    )

    list_filter = ('status', 'appointment_date', 'business')
    search_fields = (
        'customer__username',
        'business__name',
        'service__name',
    )


