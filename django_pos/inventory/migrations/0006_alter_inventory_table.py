# Generated by Django 5.0.2 on 2024-05-05 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_inventory_product'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='inventory',
            table='Inventory',
        ),
    ]