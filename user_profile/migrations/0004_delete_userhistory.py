# Generated by Django 5.1 on 2024-09-03 19:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user_profile", "0003_remove_userhistory_anime_id_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UserHistory",
        ),
    ]
