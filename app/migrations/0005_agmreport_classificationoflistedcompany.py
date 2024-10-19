# Generated by Django 5.1.1 on 2024-10-19 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_annualreport_monthlyreport"),
    ]

    operations = [
        migrations.CreateModel(
            name="AGMReport",
            fields=[
                ("SN", models.BigIntegerField(primary_key=True, serialize=False)),
                ("Name", models.TextField()),
                ("Description", models.TextField()),
                ("publishedDate", models.TextField(db_column="Published Date")),
                ("fileLink", models.TextField(db_column="File Link")),
            ],
            options={
                "db_table": "agm_reports",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="ClassificationOfListedCompany",
            fields=[
                ("SN", models.BigIntegerField(primary_key=True, serialize=False)),
                ("Name", models.TextField()),
                ("Symbol", models.TextField()),
                ("Status", models.TextField()),
                ("Sector", models.TextField()),
                ("Class", models.TextField()),
                ("Instrument", models.TextField()),
            ],
            options={
                "db_table": "listed_company",
                "managed": False,
            },
        ),
    ]
