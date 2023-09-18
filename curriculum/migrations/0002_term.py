# Generated by Django 3.2 on 2023-09-17 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='select_term', max_length=100)),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Start Date(YYYY-MM-DD)')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date(YYYY-MM-DD)')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session', to='curriculum.session')),
            ],
        ),
    ]
