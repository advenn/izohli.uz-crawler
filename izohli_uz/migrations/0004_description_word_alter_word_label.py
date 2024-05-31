# Generated by Django 5.0.6 on 2024-05-31 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("izohli_uz", "0003_alter_description_id_alter_letter_id_alter_word_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="description",
            name="word",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="izohli_uz.word",
            ),
        ),
        migrations.AlterField(
            model_name="word",
            name="label",
            field=models.TextField(unique=True),
        ),
    ]
