# Generated by Django 2.2.8 on 2019-12-21 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExpenseManager', '0013_auto_20191220_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_date', models.OneToOneField(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='ExpenseManager.Category')),
            ],
        ),
    ]
