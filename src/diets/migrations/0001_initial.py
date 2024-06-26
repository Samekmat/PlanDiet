# Generated by Django 5.0.3 on 2024-03-29 23:25

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Diet",
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
                ("name", models.CharField(max_length=124)),
                ("caloric_demand", models.IntegerField()),
                ("carbs_demand", models.IntegerField()),
                ("protein_demand", models.IntegerField()),
                ("fat_demand", models.IntegerField()),
                ("description", models.TextField()),
            ],
        ),
    ]
