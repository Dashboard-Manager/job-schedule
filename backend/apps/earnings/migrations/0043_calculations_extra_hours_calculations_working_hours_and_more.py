# Generated by Django 4.1.6 on 2023-02-13 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "earnings",
            "0042_alter_jobhours_end_date_alter_jobhours_extra_hours_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="calculations",
            name="extra_hours",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="calculations",
            name="working_hours",
            field=models.OneToOneField(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="earnings.jobhours",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="calculations",
            name="hours",
            field=models.IntegerField(default=0),
        ),
    ]
