# Generated by Django 4.2.7 on 2023-12-07 14:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shared", "0015_merge_20231205_0706"),
    ]

    operations = [
        migrations.CreateModel(
            name="CveIngestion",
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
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("valid_to", models.DateField()),
                ("delta", models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name="cverecord",
            name="triaged",
            field=models.BooleanField(default=False),
        ),
    ]
