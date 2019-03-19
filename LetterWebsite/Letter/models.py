from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
class PreferenceModel(models.Model):
    preference = models.CharField(max_length=100)
#    user = models.ForeignKey(User)
