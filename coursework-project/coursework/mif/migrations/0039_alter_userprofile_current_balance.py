# Generated by Django 4.2 on 2023-05-05 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mif", "0038_netassetvalue_valueshare_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="current_balance",
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
