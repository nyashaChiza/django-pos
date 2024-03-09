# Generated by Django 5.0.2 on 2024-03-07 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_alter_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='photo',
            field=models.ImageField(blank=True, default='/static/img/default.png', null=True, upload_to='customers'),
        ),
    ]