# Generated by Django 4.2 on 2023-04-29 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mif", "0024_userprofile_current_balance"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="current_balance",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
