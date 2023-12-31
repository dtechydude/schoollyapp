# Generated by Django 3.2 on 2023-09-18 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('description', models.CharField(blank=True, max_length=150)),
                ('item_location', models.CharField(blank=True, max_length=150)),
                ('date_recorded', models.DateField(default=None)),
                ('date_added', models.DateField(auto_now=True)),
                ('staff_in_charge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='staff.staffprofile')),
            ],
        ),
    ]
