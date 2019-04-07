# Generated by Django 2.1.5 on 2019-04-07 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Letter', '0002_auto_20190407_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='original_filename',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='userfiles', to=settings.AUTH_USER_MODEL),
        ),
    ]
