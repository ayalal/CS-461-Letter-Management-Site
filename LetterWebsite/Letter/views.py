from django.shortcuts import render, redirect
from django.http import Http404 
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
import json

from .forms import DocumentForm, ProfessorPreferencesForm, RequestForm, RequestAcceptDenyForm, DenyAcceptedRequestForm, LetterForm
from .models import Document, Letter, ProfessorPreferences, Request, LetterDoc

def get_professors():
    group_users = User.objects.filter(groups__name='Professors')
    list_users = list(group_users.values_list('username', flat=True))
    return json.dumps(list_users)

def is_professor(person):
    group = Group.objects.filter(user=person)
    if group.filter(name='Professors').exists():
        return True
    else:
        return False

def is_student(person):
    group = Group.objects.filter(user=person)
    if group.filter(name='Students').exists():
        return True
    else:
        return False


def user_exists(id):
    if User.objects.filter(id=id):
        return True
    return False

@login_required
def index(request):
    current_user = request.user
    group = Group.objects.filter(user = request.user)
    if group.filter(name='Professors').exists():
        redir = "/professor_profiles/" + str(request.user.id)
        return redirect(redir)
    elif not is_student(current_user):
        student_group = Group.objects.get(name='Students') 
        student_group.user_set.add(current_user)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('index')
    else:
        form = DocumentForm()
    documents = Document.objects.filter(user=request.user)
    json_group_users = get_professors()
    requests = Request.objects.filter(requester=request.user)
    letters = LetterDoc.objects.filter(student=request.user)
    return render(request, 'Letter/index.html', {
        'form': form,
	'documents': documents,
        'requests': requests,
        'letters': letters,
        'json_group_users': json_group_users
    })

@login_required
def professor_profiles(request, user_id):
    if not user_exists(user_id):
        raise Http404
    if not is_professor(User.objects.get(pk=user_id)):
        raise Http404
    json_group_users = get_professors()
    professor = User.objects.get(pk=user_id)                      
    if ProfessorPreferences.objects.filter(user=professor).exists():
        prefs = ProfessorPreferences.objects.get(user=professor)
    else:
        prefs = ProfessorPreferences()
        prefs.user = professor
        prefs.preferred_documents = "None"
        prefs.preferred_projects = "None"
    requests = Request.objects.filter(requestee=request.user, status=-1)
    openrequests = Request.objects.filter(requestee=request.user, status=1)
    if request.method == 'POST':
        form = RequestAcceptDenyForm(request.POST)
        denyform = DenyAcceptedRequestForm(request.POST)
        letterform = LetterForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['yes_or_no'] == 'Deny':
                requester_id = form.cleaned_data['requester_id']
                requester = User.objects.get(pk=requester_id)
                send_mail("Request Denied", "Your request for a letter was denied by the professor.", "lor@lor.com" , [requester.email])
                Request.objects.filter(
                    Q(requestee=request.user),
                    Q(requester=requester)
                ).delete()
            elif form.cleaned_data['yes_or_no'] == 'Accept':
                requester_id = form.cleaned_data['requester_id']
                requester = User.objects.get(pk=requester_id)
                send_mail("Request Accepted", "Your request for a letter was accepted by the professor.", "lor@lor.com" , [requester.email])
                Request.objects.filter(
                    Q(requestee=request.user),
                    Q(requester=requester)
                ).update(status=1)
            return redirect("/professor_profiles/"+str(request.user.id))
        elif denyform.is_valid():
            requester_id = denyform.cleaned_data['requester_id']
            requester = User.objects.get(pk=requester_id)
            send_mail("Request Denied", "Your request for a letter was denied by the professor.", "lor@lor.com" , [requester.email])
            Request.objects.filter(
                Q(requestee=request.user),
                Q(requester=requester)
            ).delete()
            return redirect("/professor_profiles/"+str(request.user.id))
        elif letterform.is_valid():
            pass
            requester_id = request.POST['student_identifier']
            print(requester_id)
            requester = User.objects.get(pk=requester_id)
            obj = letterform.save(commit=False)
            obj.user = request.user
            obj.student = requester
            obj.save()
            Request.objects.filter(
                Q(requestee=request.user),
                Q(requester=requester)
            ).delete()
        else:
            form = RequestAcceptDenyForm()
            denyform = DenyAcceptedRequestForm()
            letterform = LetterForm()
    else:
        form = RequestAcceptDenyForm() 
        denyform = DenyAcceptedRequestForm()
        letterform = LetterForm()
    return render(request, 'Letter/professor_profiles.html', {
         'form': form,
         'denyform': denyform,
         'letterform': letterform,
         'professor': professor,
         'prefs': prefs,
         'requests': requests,
         'openrequests': openrequests,
         'json_group_users': json_group_users
    })

@login_required
def student_profiles(request, user_id):
    json_group_users = get_professors()
    try:
        viewer = request.user
        person = User.objects.get(pk=user_id)
        if is_professor(person):
            redir = '/professor_profiles/' + str(user_id)
            return redirect(redir)
        if is_professor(viewer):
            documents = Document.objects.filter(user=person)
            return render(request, 'Letter/student_profiles.html', {         
                'person': person,
                'documents': documents,
                'json_group_users': json_group_users
            })
        elif person == request.user:
            return redirect('index')
        else:
            raise Http404       
    except User.DoesNotExist:
        raise Http404


@login_required
#@user_passes_test(lambda u: u.groups.filter(name='Students').count() == 1)
def request(request):
    json_group_users = get_professors()
    if request.method == 'POST':
        professor_name= request.POST['myProfessor']
        requested_professor = User.objects.get(username=professor_name)
        if ProfessorPreferences.objects.filter(user=requested_professor).exists():
            requested_professor_preferences = ProfessorPreferences.objects.get(user=requested_professor)
        else:
            requested_professor_preferences = ProfessorPreferences()
            requested_professor_preferences.user = requested_professor
            requested_professor_preferences.preferred_documents = "None"
            requested_professor_preferences.preferred_projects = "None"
        form = RequestForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.requester = request.user
            obj.requestee = User.objects.get(username=professor_name)
            obj.save()
            return redirect('index')
        else:
            form = RequestForm()
        return render(request, 'Letter/request.html',{
            'requested_professor': requested_professor,
            'requested_professor_preferences': requested_professor_preferences,
            'json_group_users': json_group_users
            })

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

@login_required
def schedule(request):
    json_group_users = get_professors()
    cid = request.user.id
    if len(list(Letter.objects.filter(student_id=cid)))==0:
        letters = list(Letter.objects.filter(professor_id=cid).order_by('date'))
    else:
        letters = list(Letter.objects.filter(student_id=cid).order_by('date'))

    #letters = filter(letters, active=True)
    #letters = filter(lamda letters: letters.active == True, letters)
    context = {
        'letters': letters,
        'letterlen': len(letters),
        'json_group_users': json_group_users
    }
    return render(request, 'Letter/schedule.html', context)

@login_required
def letter(request):
    json_group_users = get_professors()
    obj = Letter.objects.get(id=request.GET.get('id', ''))

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.user = request.user
            doc.save()
            return redirect('schedule')

    form = DocumentForm()
    documents = Document.objects.filter(user=obj.student.id)
    return render(request, 'Letter/letter.html', {
	'documents': documents,
        'object': obj,
        'json_group_users': json_group_users
    })

def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
@user_passes_test(lambda u: u.groups.filter(name='Professors').count() == 1 )
def set_preferences(request):
    json_group_users = get_professors()
    if request.method == 'POST':
        form = ProfessorPreferencesForm(request.POST)
        if form.is_valid():
            if ProfessorPreferences.objects.filter(user=request.user).exists():
                ProfessorPreferences.objects.filter(user=request.user).delete()
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            text = request.POST.get('Submit', None)
            redir = "/professor_profiles/" + str(request.user.id)
            return redirect(redir)
    else :
        form = ProfessorPreferencesForm
    return render(request, 'Letter/preferences_form.html', {
        'form': form,
        'json_group_users': json_group_users
    })

@login_required
def delete_file(request, document_id):
    file = Document.objects.get(pk=document_id)
    Document.objects.get(pk=document_id).delete()
    return redirect('/')
