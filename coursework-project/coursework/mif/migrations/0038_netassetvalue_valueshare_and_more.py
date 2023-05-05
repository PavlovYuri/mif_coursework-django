# Generated by Django 4.2 on 2023-05-04 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mif", "0037_alter_analyticalplan_quantity"),
    ]

    operations = [
        migrations.CreateModel(
            name="NetAssetValue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("net_asset_value", models.FloatField(null=True)),
                ("date", models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="ValueShare",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("value_share", models.FloatField(null=True)),
                ("date", models.DateField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name="findistribution",
            old_name="net_asset_value",
            new_name="current_net_asset_value",
        ),
    ]