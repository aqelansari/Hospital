from django.contrib import admin
from .models import Appointment


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'counsellor', 'appointment_date', 'is_active')
    search_fields = ['patient__name', 'counsellor__name', 'appointment_date']

admin.site.register(Appointment, AppointmentAdmin)
