# Generated by Django 5.0.2 on 2024-05-28 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etims', '0005_alter_itemclasscodes_itemclasscodename'),
    ]

    operations = [
        migrations.CreateModel(
            name='EtimsProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
