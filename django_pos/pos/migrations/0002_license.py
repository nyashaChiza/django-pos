# Generated by Django 5.0.2 on 2024-03-06 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('expires', models.DateTimeField()),
                ('company_id', models.IntegerField()),
            ],
            options={
                'verbose_name': 'License',
                'verbose_name_plural': 'Licenses',
            },
        ),
    ]