# Generated by Django 4.1.7 on 2023-04-18 13:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0008_add_proposal_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vote",
            name="in_favor",
            field=models.BooleanField(db_index=True, null=True),
        ),
    ]
