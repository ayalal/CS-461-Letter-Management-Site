# Generated by Django 2.2a1 on 2019-04-15 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Letter', '0008_auto_20190415_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='professor',
            new_name='requestee',
        ),
        migrations.RenameField(
            model_name='request',
            old_name='student',
            new_name='requester',
        ),
    ]
