from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import PreferenceForm
from .models import PreferenceModel

def index(request):
    return render(request, 'Letter/index.html')

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'Letter/upload.html')

def get_preference(request):
    if request.method == 'POST':
        form = PreferenceForm(request.POST)
        if form.is_valid():
            form.save()
#            preferenceObj = form.save(commit=False)
#            preferenceObj.save()
       #     preferenceObj.user = request.user
            text = form.cleaned_data['preference'] #pick up variable
            form = PreferenceForm
#            return redirect('/')
            args = {'form': form, 'preference': text} # args to pass
            return render(request, 'Letter/preference.html', args)
        return render(request, 'Letter/preference.html')
    else:
        form = PreferenceForm()
        preferences = PreferenceModel.objects.all()

        args = {'form': form, 'preferences': preferences}
        return render(request, 'Letter/preference.html', args)

def view_preference(request):
    
    return render(request, 'Letter/preferences.html',)

#this is a tmeporary page sor user sign in/sign up. This won't be needed once connected to CAS
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'Letter/register.html', {'form': form})

def schedule(request):
	return render(request, 'Letter/schedule.html')

def letter(request):
	return render(request, 'Letter/letter.html')

#def user_login(request):
#    username = request.POST['username']

#def logout(request):
#    return render(request, 'Letter/logout.html')
