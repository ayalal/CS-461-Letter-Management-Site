from django import forms
from django.contrib.auth.models import User
from .models import Document, ProfessorPreferences, Request, LetterDoc

REQUEST_CHOICES=[('Accept', 'Accept'),
                 ('Deny', 'Deny')]

class ProfessorPreferencesForm(forms.ModelForm):
    class Meta:
        model = ProfessorPreferences
        fields = ('preferred_documents', 'preferred_projects',)

class LetterForm(forms.ModelForm):
    class Meta:
        model = LetterDoc
        widgets = {'student': forms.HiddenInput()}
        fields = ('document',)

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('date_initiated',)


class DenyAcceptedRequestForm(forms.Form):
    requester_id = forms.IntegerField(widget=forms.HiddenInput())

    def clean(self):
        cleaned_data = super(DenyAcceptedRequestForm, self).clean()
        requester_id = cleaned_data.get('requester_id')
        if not requester_id:
            print("error with form")
            raise forms.ValidationError('Internal Error with request')


class RequestAcceptDenyForm(forms.Form):
    yes_or_no = forms.ChoiceField(choices=REQUEST_CHOICES, widget=forms.RadioSelect)
    requester_id = forms.IntegerField(widget=forms.HiddenInput())

    def clean(self):
        cleaned_data = super(RequestAcceptDenyForm, self).clean()
        yes_or_no = cleaned_data.get('yes_or_no')
        requester_id = cleaned_data.get('requester_id')
        if not yes_or_no:
            raise forms.ValidationError('Choice required')
        if not requester_id:
            raise forms.ValidationError('Internal Error with request')