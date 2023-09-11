# Generated by Django 3.2 on 2023-09-11 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0001_initial'),
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('description', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentChart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('term', models.CharField(blank=True, choices=[('first_term', 'first_term'), ('second_term', 'second_term'), ('third_term', 'third_term'), ('others', 'others')], max_length=50)),
                ('amount_due', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('payment_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.paymentcategory')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.session')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, null=True)),
                ('description', models.CharField(blank=True, max_length=200)),
                ('payment_date', models.DateField()),
                ('installment_level', models.CharField(choices=[('First_payment', 'First_payment'), ('Second_payment', 'Second_payment'), ('Third_payment', 'Third_payment'), ('Fourth_payment', 'Fourth_payment'), ('Complete_once', 'Complete_once')], default='select_installment', max_length=50)),
                ('payment_method', models.CharField(choices=[('cash', 'cash'), ('bank_deposit', 'bank_deposit'), ('bank_transfer', 'bank_transfer'), ('cheque', 'cheque'), ('pos', 'pos')], max_length=50)),
                ('depositor', models.CharField(max_length=150)),
                ('bank_name', models.CharField(max_length=150)),
                ('teller', models.CharField(blank=True, max_length=150)),
                ('confirmed', models.BooleanField(default=False)),
                ('payment_recorded_date', models.DateField(auto_now_add=True)),
                ('payee', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('payment_name', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='payment.paymentchart')),
                ('student_detail', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.studentdetail')),
            ],
            options={
                'ordering': ['-payment_date'],
            },
        ),
    ]
