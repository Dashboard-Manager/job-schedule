# Generated by Django 4.1.5 on 2023-02-01 18:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("earnings", "0019_alter_jobhours_start_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobhours",
            name="end_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="jobhours",
            name="start_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
