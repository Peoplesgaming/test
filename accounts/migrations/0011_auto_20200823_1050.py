# Generated by Django 3.1 on 2020-08-23 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200822_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='Saftey_concern',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
