from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
import os
import datetime

# Create your models here.
class ProfessorPreferences(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    preferred_documents = models.CharField(max_length=200)
    preferred_projects = models.CharField(max_length=200)

def user_directory_path(instance, filename):
    return 'user_{0}/myUploads/{1}'.format(instance.user.id, filename)

def user_letter_path(instance, filename):
    return 'user_{0}/myLetters/{1}'.format(instance.user.id, filename)

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def filename(self):
        return os.path.basename(self.document.name)

#model used for letters of Recommendation
class LetterDoc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userletters')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_letter')
    document = models.FileField(upload_to=user_letter_path)
    uploaded_at = models.DateField(_("Date"), default=datetime.date.today, blank=True, null=True)

    def filename(self):
        return os.path.basename(self.document.name)

class Request(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requester')
    requestee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requestee')
    date_initiated = models.DateField(_("Date"), default=datetime.date.today, blank=True, null=True)
    status = models.IntegerField(default=-1)
    def __str__(self):
        return self.requester.username

# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_delete, sender=Document)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `document` object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)

@receiver(models.signals.pre_save, sender=Document)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `document` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = Document.objects.get(pk=instance.pk).file
    except Document.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)


class Letter(models.Model):
    student = models.ForeignKey(User, related_name="student", on_delete=models.CASCADE)
    professor = models.ForeignKey(User, related_name="professor", on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.student.username
