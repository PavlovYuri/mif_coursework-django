# Generated by Django 4.2 on 2023-04-24 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("mif", "0003_remove_userprofile_user_delete_employeeprofile_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                ("username", models.CharField(max_length=250)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone_number", models.CharField(max_length=20)),
                ("password", models.CharField(max_length=250)),
            ],
        ),
    ]