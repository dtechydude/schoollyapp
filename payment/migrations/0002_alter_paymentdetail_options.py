# Generated by Django 3.2 on 2023-09-07 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paymentdetail',
            options={'ordering': ['-payment_date']},
        ),
    ]
