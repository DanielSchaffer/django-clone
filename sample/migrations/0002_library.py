# Generated by Django 2.2.7 on 2019-11-04 13:46
import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import model_clone.mixin


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("sample", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Library",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            bases=(model_clone.mixin.CloneMixin, models.Model),
        ),
    ]
