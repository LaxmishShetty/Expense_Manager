# Generated by Django 2.2.8 on 2020-01-02 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(blank=True, default='Cake', max_length=20, null=True)),
                ('total_expense', models.IntegerField(blank=True, default=0, null=True)),
                ('datefield', models.DateField(blank=True, default='2012-12-12', null=True)),
                ('petrol_total_expense', models.IntegerField(blank=True, default=0, null=True)),
                ('clothes_total_expense', models.IntegerField(blank=True, default=0, null=True)),
                ('cloth_type', models.CharField(blank=True, default='Jeans', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateField', models.DateField(blank=True, default='2019-01-01')),
                ('food_expense', models.IntegerField(blank=True, default=1, null=True)),
                ('petrol_expense', models.IntegerField(blank=True, default=1, null=True)),
                ('cloth_expense', models.IntegerField(blank=True, default=1, null=True)),
                ('total_expense', models.IntegerField(blank=True, default=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_site', models.URLField(blank=True)),
                ('bio', models.CharField(blank=True, max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
