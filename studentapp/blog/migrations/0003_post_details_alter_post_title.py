# Generated by Django 5.1.3 on 2024-12-20 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_feedback"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="details",
            field=models.TextField(default=""),
        ),
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]