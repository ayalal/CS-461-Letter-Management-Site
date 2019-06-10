# Generated by Django 2.2a1 on 2019-04-15 18:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Letter', '0007_auto_20190414_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_initiated', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requestee', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requester', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
