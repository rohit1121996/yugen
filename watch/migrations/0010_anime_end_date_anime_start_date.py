# Generated by Django 5.1 on 2024-09-03 21:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("watch", "0009_anime_z_anime_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="anime",
            name="end_date",
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name="anime",
            name="start_date",
            field=models.DateField(null=True),
        ),
    ]
