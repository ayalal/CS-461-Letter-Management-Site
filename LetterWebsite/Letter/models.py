from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


class PreferenceModel(models.Model):
    preference = models.CharField(max_length=100)
#    user = models.ForeignKey(User)

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
