# Generated by Django 5.1 on 2024-09-04 00:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_profile", "0008_userhistory"),
    ]

    operations = [
        migrations.AddField(
            model_name="userhistory",
            name="last_watched",
            field=models.BooleanField(default=False),
        ),
    ]
