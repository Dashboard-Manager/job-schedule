# Generated by Django 4.1.5 on 2023-02-01 17:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("earnings", "0007_alter_jobhours_start_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobhours",
            name="start_date",
            field=models.DateField(
                default=datetime.datetime(2023, 1, 31, 17, 27, 15, 899839)
            ),
        ),
    ]
