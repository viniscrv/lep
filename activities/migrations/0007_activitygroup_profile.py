# Generated by Django 5.0.3 on 2024-03-16 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0006_activitygroup_activity_activity_group'),
        ('profiles', '0002_rename_profile_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitygroup',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile'),
            preserve_default=False,
        ),
    ]
