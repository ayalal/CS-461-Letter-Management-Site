from django.contrib import admin

from .models import Letter
from .models import Document
#from .models import LetterDoc
from .models import ProfessorPreferences
from .models import Request

#class LetterAdmin(admin.ModelAdmin):
#    list_display = ('id', 'student_id', 'professor_id', 'active')

# Register your models here.
#admin.site.register(Letter, LetterAdmin)
admin.site.register(Letter)
admin.site.register(Document)
#admin.site.register(LetterDoc)
admin.site.register(ProfessorPreferences)
admin.site.register(Request)
