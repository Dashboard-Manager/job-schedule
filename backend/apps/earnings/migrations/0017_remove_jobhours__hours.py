# Generated by Django 4.1.5 on 2023-02-01 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("earnings", "0016_jobhours__hours"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="jobhours",
            name="_hours",
        ),
    ]
