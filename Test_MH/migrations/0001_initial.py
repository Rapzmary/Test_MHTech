# Generated by Django 4.1.3 on 2022-11-16 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="register",
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
                ("firstname", models.CharField(max_length=255)),
                ("lastname", models.CharField(max_length=255)),
                ("email", models.CharField(max_length=255)),
                ("password", models.CharField(max_length=255)),
            ],
        ),
    ]
