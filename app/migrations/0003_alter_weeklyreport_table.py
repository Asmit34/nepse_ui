# Generated by Django 5.1.1 on 2024-10-17 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_weeklyreport_table"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="weeklyreport",
            table="weekly_reports",
        ),
    ]
