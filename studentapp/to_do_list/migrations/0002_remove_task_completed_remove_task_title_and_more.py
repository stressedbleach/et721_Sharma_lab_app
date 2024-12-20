# Generated by Django 5.1.3 on 2024-12-20 13:05

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("to_do_list", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="completed",
        ),
        migrations.RemoveField(
            model_name="task",
            name="title",
        ),
        migrations.AddField(
            model_name="task",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="task",
            name="task",
            field=models.CharField(default="Default Task", max_length=255),
            preserve_default=False,
        ),
    ]
