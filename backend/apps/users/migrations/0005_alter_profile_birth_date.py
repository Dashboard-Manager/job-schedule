# Generated by Django 4.1.6 on 2023-02-15 21:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_profile_birth_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="birth_date",
            field=models.DateField(
                default=datetime.datetime(
                    2007, 2, 19, 21, 25, 47, 992550, tzinfo=datetime.timezone.utc
                ),
                verbose_name="Birth date",
            ),
        ),
    ]