# Generated by Django 4.2 on 2023-04-26 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mif", "0011_alter_findistribution_current_value_share"),
    ]

    operations = [
        migrations.AlterField(
            model_name="findistribution",
            name="current_value_share",
            field=models.FloatField(null=True),
        ),
    ]