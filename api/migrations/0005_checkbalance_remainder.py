# Generated by Django 4.1.1 on 2022-10-06 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_alter_checkbalance_actives_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="checkbalance",
            name="remainder",
            field=models.IntegerField(default=0),
        ),
    ]