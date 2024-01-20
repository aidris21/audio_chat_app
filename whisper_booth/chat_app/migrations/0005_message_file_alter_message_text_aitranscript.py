# Generated by Django 4.1 on 2024-01-20 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("chat_app", "0004_remove_message_to_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="message",
            name="file",
            field=models.FileField(null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="message",
            name="text",
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.CreateModel(
            name="AITranscript",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField(max_length=500, null=True)),
                ("at_time", models.DateTimeField()),
                (
                    "to_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="to_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
