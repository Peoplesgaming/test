# Generated by Django 3.1 on 2020-08-22 14:50

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_staff_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='leave_from',
            field=models.DateTimeField(null=True, verbose_name=accounts.models.requests),
        ),
    ]
