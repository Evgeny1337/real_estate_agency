from django.contrib import admin
from .models import Flat, Complaint


class AuthorAdmin(admin.ModelAdmin):
    raw_id_fields = ["liked_by"]
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price',
                    'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat', 'user']


admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Flat, AuthorAdmin)
