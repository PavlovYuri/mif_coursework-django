# Generated by Django 4.2 on 2023-04-29 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mif", "0025_alter_userprofile_current_balance"),
    ]

    operations = [
        migrations.AddField(
            model_name="employeeprofile",
            name="bank_card_number",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
