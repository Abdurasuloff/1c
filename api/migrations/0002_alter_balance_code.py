# Generated by Django 4.1.1 on 2022-10-04 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="balance",
            name="code",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
