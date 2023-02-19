# Generated by Django 4.1.5 on 2023-02-19 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("main", "0002_alter_clothes_likes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="talk",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="talk_user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
