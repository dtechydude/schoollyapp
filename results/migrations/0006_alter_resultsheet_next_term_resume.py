# Generated by Django 3.2 on 2023-09-06 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0005_auto_20230906_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultsheet',
            name='next_term_resume',
            field=models.DateField(blank=True, null=True),
        ),
    ]
