# Generated by Django 5.0.1 on 2024-01-21 15:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superusers', '0005_alter_users_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrecord',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='account',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 21, 21, 17, 55, 427033), null=True),
        ),
    ]
