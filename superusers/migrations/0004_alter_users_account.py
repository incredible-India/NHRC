# Generated by Django 5.0.1 on 2024-01-21 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superusers', '0003_alter_users_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='account',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 21, 20, 49, 27, 681024), null=True),
        ),
    ]
