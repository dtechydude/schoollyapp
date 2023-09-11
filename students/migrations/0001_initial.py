# Generated by Django 3.2 on 2023-09-11 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('last_class', models.CharField(max_length=150)),
                ('new_class', models.CharField(max_length=150)),
                ('application_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_username', models.CharField(max_length=20, unique=True)),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('is_prefect', models.BooleanField(default=False)),
                ('student_type', models.CharField(choices=[('day_student', 'day_student'), ('boarder', 'boarder')], default='day_student', max_length=15)),
                ('address', models.CharField(blank=True, max_length=120, null=True)),
                ('region_origin', models.CharField(choices=[('Select', 'Select'), ('SouthWest', 'SouthWest'), ('SouthEast', 'SouthEast'), ('SouthSouth', 'SouthSouth'), ('NorthWest', 'NorthWest'), ('NorthEast', 'NorthEast'), ('NorthCentral', 'NorthCentral')], default='Select', max_length=20)),
                ('gender', models.CharField(choices=[('female', 'female'), ('male', 'male'), ('select_gender', 'select_gender')], default='select_gender', max_length=20)),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of Birth (YYYY-MM-DD)')),
                ('date_admitted', models.DateField(verbose_name='Admission date (YYYY-MM-DD)')),
                ('guardian_name', models.CharField(max_length=60)),
                ('guardian_address', models.TextField(blank=True, max_length=120)),
                ('guardian_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('guardian_email', models.CharField(blank=True, max_length=30, null=True)),
                ('relationship', models.CharField(choices=[('father', 'father'), ('mother', 'mother'), ('sister', 'sister'), ('brother', 'brother'), ('aunt', 'aunt'), ('uncle', 'uncle'), ('other', 'other'), ('select', 'select')], default='select', max_length=25)),
                ('student_status', models.CharField(choices=[('active', 'active'), ('graduated', 'graduated'), ('dropped', 'dropped'), ('expelled', 'expelled')], default='active', max_length=15)),
                ('badge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.badge')),
                ('class_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.classgroup')),
                ('class_on_admission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentdetails', to='curriculum.standard', verbose_name='class_on_admission')),
                ('class_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staffprofile')),
                ('current_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.standard')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='student_username')),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='Mystudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(blank=True, max_length=150)),
                ('year', models.CharField(blank=True, max_length=150)),
                ('institution', models.CharField(blank=True, max_length=150)),
                ('professional_body', models.CharField(blank=True, max_length=150)),
                ('academic', models.CharField(blank=True, max_length=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
