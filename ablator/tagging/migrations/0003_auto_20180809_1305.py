# Generated by Django 2.0.6 on 2018-08-09 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_management", "0001_initial"),
        ("tagging", "0002_auto_20180809_1141"),
    ]

    operations = [
        migrations.AlterUniqueTogether(name="tag", unique_together={("name", "organization")},),
    ]
