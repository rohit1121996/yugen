# Generated by Django 5.1 on 2024-09-04 00:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_profile", "0009_userhistory_last_watched"),
    ]

    operations = [
        migrations.AddField(
            model_name="userhistory",
            name="time_watched",
            field=models.IntegerField(default=0),
        ),
    ]
