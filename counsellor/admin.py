from django.contrib import admin
from .models import Counsellor


class CounsellorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_active')
    search_fields = ['name', 'email']

admin.site.register(Counsellor, CounsellorAdmin)
