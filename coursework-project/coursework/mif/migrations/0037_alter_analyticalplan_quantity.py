# Generated by Django 4.2 on 2023-05-02 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mif", "0036_analyticalplan_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="analyticalplan",
            name="quantity",
            field=models.IntegerField(null=True),
        ),
    ]
