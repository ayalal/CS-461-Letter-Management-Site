from django import forms
from django.contrib.auth.models import User
from .models import PreferenceModel, Document

class PreferenceForm(forms.ModelForm):
    preference = forms.CharField(label='preference', max_length=100)
    class Meta:
        model = PreferenceModel
        fields = ('preference',)

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document',)
