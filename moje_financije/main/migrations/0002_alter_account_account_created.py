# Generated by Django 5.1.4 on 2024-12-18 19:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="account_created",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 12, 18, 19, 51, 48, 550122, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]