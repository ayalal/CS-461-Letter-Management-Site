from django import forms
from django.contrib.auth.models import User
from .models import Document, ProfessorPreferences, LetterDoc, Request

class ProfessorPreferencesForm(forms.ModelForm):
    class Meta:
        model = ProfessorPreferences
        fields = ('preferred_documents', 'preferred_projects',)

class LetterForm(forms.ModelForm):
    class Meta:
        model = LetterDoc
        fields = ('sharedWith', 'description', 'document',)

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('date_initiated',)
