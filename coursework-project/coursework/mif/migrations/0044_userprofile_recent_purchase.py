# Generated by Django 4.2 on 2023-05-06 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mif", "0043_userprofile_opened_personal_account"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="recent_purchase",
            field=models.IntegerField(null=True),
        ),
    ]
