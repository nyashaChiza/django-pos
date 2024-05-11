# Generated by Django 5.0.2 on 2024-05-11 17:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_alter_company_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='bill_template_id',
        ),
        migrations.RemoveField(
            model_name='company',
            name='invoice_template_id',
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('branch_id', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branches',
                'db_table': 'Branch',
            },
        ),
    ]
