# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-13 10:56


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("budgetportal", "0019_event")]

    operations = [
        migrations.AddField(
            model_name="event",
            name="status",
            field=models.CharField(
                choices=[(b"upcoming", b"upcoming"), (b"past", b"past")],
                default=b"upcoming",
                max_length=255,
            ),
        )
    ]
