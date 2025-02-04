# Generated by Django 5.1.3 on 2025-02-03 23:42

import uuid
import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("management", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="activity",
            name="estimated_duration",
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AlterField(
            model_name="activity",
            name="instructor",
            field=models.CharField(max_length=150, verbose_name="Monitor"),
        ),
        migrations.AlterField(
            model_name="activity",
            name="title",
            field=models.CharField(max_length=150, verbose_name="Título"),
        ),
        migrations.AlterField(
            model_name="event",
            name="title",
            field=models.CharField(max_length=150, verbose_name="Título"),
        ),
        migrations.CreateModel(
            name="Certificate",
            fields=[
                (
                    "certificate_id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("duration", models.DurationField()),
                (
                    "activity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="management.activity",
                    ),
                ),
            ],
        ),
    ]
