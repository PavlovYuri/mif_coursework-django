# Generated by Django 4.2 on 2023-04-29 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mif", "0022_depositoryinstance_is_processed_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="employeeprofile",
            name="salary",
            field=models.FloatField(null=True),
        ),
    ]