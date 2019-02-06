from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request, 'Letter/index.html')

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
    #    print(uploaded_file.name)
    #    print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'Letter/upload.html')
