from django import forms
from django.contrib.auth.models import User
from .models import PreferenceModel

class PreferenceForm(forms.ModelForm):
    preference = forms.CharField(label='preference', max_length=100)
    class Meta:
        model = PreferenceModel
        fields = ('preference',)

