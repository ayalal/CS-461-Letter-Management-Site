# Generated by Django 2.2a1 on 2019-04-07 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Letter', '0004_document_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
