# Generated by Django 5.0.3 on 2024-03-29 23:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("diets", "0001_initial"),
        ("exercises", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Plan",
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
                ("name", models.CharField(max_length=60)),
                (
                    "diet",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="diets.diet",
                    ),
                ),
                (
                    "exercises",
                    models.ManyToManyField(default=None, to="exercises.exercise"),
                ),
            ],
        ),
    ]
