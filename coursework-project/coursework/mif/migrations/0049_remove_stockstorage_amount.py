# Generated by Django 4.2 on 2023-05-06 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mif", "0048_remove_stockstorage_datetime_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="stockstorage",
            name="amount",
        ),
    ]
