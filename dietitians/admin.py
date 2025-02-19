from django.contrib import admin
from django.utils.html import format_html
from .models import Dietitian

class DietitianAdmin(admin.ModelAdmin):
    list_display = ("user", "licence_number", "view_documents") 
    def view_documents(self, obj):
        if obj.diploma:
            return format_html('<a href="{}" target="_blank">View Diploma</a>', obj.diploma.url)
        return "No Document"
    view_documents.short_description = "Documents"

admin.site.register(Dietitian, DietitianAdmin)