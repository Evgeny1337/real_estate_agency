from django.contrib import admin
from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Flat.owners.through
    extra = 1
    raw_id_fields = ['owner']


@admin.register(Flat)
class AuthorAdmin(admin.ModelAdmin):
    raw_id_fields = ["liked_by"]
    search_fields = ['town', 'address', 'owners__fio']
    readonly_fields = ['created_at']
    list_display = ['address', 'price',
                    'new_building', 'construction_year', 'town', 'pure_number', 'number']

    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']

    def number(self, obj):
        owner = obj.owners.first()
        return owner.number if owner else None

    def pure_number(self, obj):
        owner = obj.owners.first()
        return owner.pure_number if owner else None

    number.short_description = 'Номер владельца'
    pure_number.short_description = 'Нормализированный номер владельца'

    inlines = [OwnerInline]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat', 'user']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']
