# Generated by Django 5.1 on 2024-09-03 23:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("watch", "0018_remove_anime_title_remove_anime_trailer_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animeepisode",
            name="episode_number",
            field=models.IntegerField(),
        ),
    ]
