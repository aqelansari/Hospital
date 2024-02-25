from django.contrib import admin
from  .models import Patient


class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_active')
    search_fields = ['name', 'email']

admin.site.register(Patient, PatientAdmin)


