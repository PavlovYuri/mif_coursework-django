# Generated by Django 4.2 on 2023-05-02 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mif", "0030_analiticsplan_quantity"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="AnaliticsPlan",
            new_name="AnalyticalPlan",
        ),
    ]
