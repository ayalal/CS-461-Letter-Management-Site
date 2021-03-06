# Generated by Django 2.2a1 on 2019-05-16 22:55

import Letter.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Letter', '0011_request_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='LetterDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to=Letter.models.user_letter_path)),
                ('uploaded_at', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Date')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_letter', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userletters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
