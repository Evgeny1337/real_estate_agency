from django.contrib import admin
from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Flat.owners.through
    extra = 1
    raw_id_fields = ['owner']


@admin.register(Flat)
class AuthorAdmin(admin.ModelAdmin):
    raw_id_fields = ["liked_by"]
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address', 'price',
                    'new_building', 'construction_year', 'town', 'owner_pure_phone', 'owners_phonenumber']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    inlines = [OwnerInline]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat', 'user']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']
