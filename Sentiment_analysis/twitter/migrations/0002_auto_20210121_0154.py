# Generated by Django 3.1.5 on 2021-01-21 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("twitter", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Users",
            new_name="Usernames",
        ),
    ]
