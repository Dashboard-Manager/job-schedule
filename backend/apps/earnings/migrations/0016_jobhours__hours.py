# Generated by Django 4.1.5 on 2023-02-01 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("earnings", "0015_alter_jobhours_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobhours",
            name="_hours",
            field=models.IntegerField(db_column="hours", default=0),
        ),
    ]
