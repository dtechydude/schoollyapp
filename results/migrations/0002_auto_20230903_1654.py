# Generated by Django 3.2 on 2023-09-03 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('results', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resultsheet',
            old_name='student',
            new_name='student_detail',
        ),
        migrations.AddField(
            model_name='resultsheet',
            name='student_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
