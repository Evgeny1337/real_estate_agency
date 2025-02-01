# Generated by Django 2.2.24 on 2025-02-01 14:45

from django.db import migrations


class Migration(migrations.Migration):
    def fill_owners(apps, schema_editor):
        Flat = apps.get_model('property', 'Flat')
        Owner = apps.get_model('property', 'Owner')
        for flat in Flat.objects.all():
            owner = Owner.objects.filter(
                fio=flat.owner, number=flat.owners_phonenumber)
            if not owner:
                owner = Owner.objects.create(
                    fio=flat.owner,
                    number=flat.owners_phonenumber,
                    pure_number=flat.owner_pure_phone
                )
            owner.flats.add(flat)
            owner.save()

    dependencies = [
        ('property', '0016_auto_20250201_1937'),
    ]

    operations = [
        migrations.RunPython(fill_owners)
    ]
