# Generated by Django 5.1 on 2024-09-03 21:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("watch", "0008_alter_anime_totalepisodes"),
    ]

    operations = [
        migrations.AddField(
            model_name="anime",
            name="z_anime_id",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
