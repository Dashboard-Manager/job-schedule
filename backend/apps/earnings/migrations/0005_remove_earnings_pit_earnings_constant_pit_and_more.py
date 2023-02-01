# Generated by Django 4.1.5 on 2023-01-29 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("earnings", "0004_earnings_constant_disability_contribution_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="earnings",
            name="PIT",
        ),
        migrations.AddField(
            model_name="earnings",
            name="constant_PIT",
            field=models.FloatField(default=12, verbose_name="PIT tax"),
        ),
        migrations.AlterField(
            model_name="earnings",
            name="constant_disability_contribution",
            field=models.FloatField(
                default=1.5, verbose_name="Disability Contribution"
            ),
        ),
        migrations.AlterField(
            model_name="earnings",
            name="constant_health_care_contribution",
            field=models.FloatField(default=9, verbose_name="Health Care Contribution"),
        ),
        migrations.AlterField(
            model_name="earnings",
            name="constant_pension_contribution",
            field=models.FloatField(default=9.78, verbose_name="Pension Contribution"),
        ),
        migrations.AlterField(
            model_name="earnings",
            name="constant_sickness_contribution",
            field=models.FloatField(default=2.45, verbose_name="Sickness Contribution"),
        ),
    ]