# Generated by Django 4.2 on 2023-05-05 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mif", "0041_findistribution_all_shares_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="is_processed",
            field=models.BooleanField(default=False),
        ),
    ]
