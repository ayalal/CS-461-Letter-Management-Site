from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import *
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os

def index(request):
    return render(request, 'Letter/index.html')

# def upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['document']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         print(fs.url(filename))
#         path = default_storage.save(filename, ContentFile(myfile.read()))
#         print(path)
#     return render(request, 'core/simple_upload.html')


def login(request):
    return render(request, 'Letter/login.html', {'flag': '0'})

# check login for student and teacher
def checkLogin(request):
   username = request.POST['username']
   psw = request.POST['password']
   role = request.POST['role']
   #Student login
   if role == 'student':
       try:
          stu = Student.objects.get(sname = username)
       except:
           return render(request, 'Letter/login.html',{'flag':'1' , 'msg':'user not exist'})
       else:
           if stu.psw == psw :
               print('学生登陆成功')
               request.session['id']=stu.id
               request.session['name']=stu.sname
               return redirect('initStuIndex')
           else:
               return render(request, 'Letter/login.html',{'flag':'1' , 'msg':'password not correct'})

   #Teacher login
   else:
       try:
           tea = Teacher.objects.get(tname=username)
       except:
           return render(request, 'Letter/login.html', {'flag': '1', 'msg': 'user not exist'})
       else:
           if tea.psw == psw:
               print('教师登陆成功')
               toUrl = '/index_tea/'+str(tea.id)+'/'
               print(toUrl)
               return redirect(toUrl)
           else:
               return render(request, 'Letter/login.html', {'flag': '1', 'msg': 'password not correct'})

# Student Index
def  initStuIndex(request):
    #Get login user
    sid = request.session.get('id')
    stu = Student.objects.get(id=sid)
    contents= Content.objects.filter(stuid=sid)
    #get teacher name
    for content in contents:
        try:
            tea = Teacher.objects.get(id = content.teaid)
        except:
            content.teaname = ''
        else:
            content.teaname = tea.tname
    #get file from student and teacher
    for content in contents:
        try:
            sfile = Fileinfo.objects.get(id = content.stufileid)
        except:
            content.stufileposition = ''
        else:
            content.stufileposition = sfile.position
        try:
            tfile = Fileinfo.objects.get(id = content.teafileid)
        except:
            content.teafileposition = ''
        else:
            content.teafileposition = tfile.position

    #get request progress
    for content in contents:
        #1. no progress
        if content.feedback == '':
            content.progress.append('NO FEEDBACK')
        elif content.teafileid == '':
            content.progress.append('NO TEACHER FILE')
        else:
            content.progress='FINISH'
    #get teacher by department

    #get my request
    #get my upload
    return  render(request,'Letter/index_stu.html',{'stu':stu,'contents':contents})

# Register
def register(request):
    return render(request, 'Letter/register.html', {'flag': 0})
def registerCheck(request):
    #Correct Data
    user = request.POST['username']
    psw = request.POST['password']
    psw2 = request.POST['password2']
    department = request.POST['department']
    role = request.POST['role']
    #Student Register
    if role == 'student':
        if user == '' or user is None or psw =='' or psw is None or psw2=='' or psw2 is None:
            return render(request,'Letter/register.html',{'flag':1,'msg':'Can not be empty'})
        if psw !=psw2:
            return render(request, 'Letter/register.html', {'flag': 1, 'msg': 'Password not the same'})
        try:
            stu = Student.objects.filter(sname=user)
        except:
            return render(request, 'Letter/register.html', {'flag': 1, 'msg': 'Error'})
        else:
            if len(stu)>1:
                return render(request, 'Letter/register.html', {'flag': 1, 'msg': 'User Exist!'})
            stu2 = Student()
            stu2.sname = user
            stu2.psw = psw
            stu2.save()
            return render(request, 'Letter/register.html', {'flag': 1, 'msg': 'Register Success'})

    #Teacher Register
    if user == '' or user is None or psw == '' or psw is None or psw2 == '' or psw2 is None or department=='' or department is None:
        return render(request, 'Letter/register.html', {'flag': 1, 'msg': 'Can not be empty'})
    if psw != psw2:
        return render(request, 'Letter/register.html', {'flag': 1, 'msg': 'Password not the same'})
    try:
        teacher = Teacher.objects.filter(tname=user)
    except:
        return render(request, 'Letter/register.html', {'flag': 1, 'msg': 'Error'})
    else:
        if len(teacher) > 1:
            return render(request, 'Letter/register.html', {'flag': 1, 'msg': 'User Exist!'})
        teacher2 = Teacher()
        teacher2.tname=user
        teacher2.psw=psw
        teacher2.department=department
        teacher2.save()
        return render(request, 'Letter/register.html', {'flag': 1, 'msg': 'Register Success'})

    return render(request,'Letter/register.html')

# SearchTeacher
def searchTeacher(request,sid):
    return render(request,'Letter/search.html')

def searchByDepartment(request):
    department = request.POST['department']
    teachers = Teacher.objects.filter(department=department)
    print(teachers)
    return  render(request,'Letter/search.html',{'teachers':teachers})

# Upload File for student and teacher
def upload(request,uid):
    #Storage file to local file system
    if request.method == 'POST' and request.FILES['document']:
        myfile = request.FILES['document']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        print(filename)
        # path = default_storage.save(filename, ContentFile(myfile.read()))
        # Record file info to mysql
        file = Fileinfo()
        file.position = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'media')
        file.position = file.position+filename
        print(file.position)
        if len(filename.split('.')) > 1:
            file.format = filename.split('.')[1]
        else:
            file.format = ''
        file.uid=uid
        file.save()
    return redirect('initStuIndex')

# Make new request
def makeRequest(request,uid):
    #Get student file
    files = Fileinfo.objects.filter(uid=uid)
    #Get all teacher
    teachers = Teacher.objects.all()
    return render(request, 'Letter/new_request.html', {'files': files,'teachers':teachers})

def submitRequest(request,uid):
    content = Content();
    file = request.POST['fileid']
    tid = request.POST['teacherid']
    requirement = request.POST['requirement']
    content.stufileid = file
    content.teaid = tid
    content.stuid = uid
    content.requirement = requirement
    content.save()
    return redirect('initStuIndex')

def initTeacher(request,uid):
    #get student info
    print(uid)
    contents = Content.objects.filter(teaid=uid)
    for content in contents:
        try:
            stu = Student.objects.get(id=content.stuid)
        except:
            content.sname = ''
        else:
            content.sname = stu.sname
    teacher = Teacher.objects.get(id=uid)
    return render(request, 'Letter/index_tea.html', {'contents': contents, 'teacher': teacher})
    #return render(request, 'Letter/index_tea.html')

#Feedback
def feedback(request,uid,contentid):
    #write feedback
    feed = request.POST['preference']
    content = Content.objects.get(id=contentid)
    content.feedback = feed
    content.save()
    path = '/index_tea/' + str(uid)
    return redirect(path)

#Upload for teacher
def uploadTeacherFile(request,uid,contentid):
    #storage to local
    if request.method == 'POST' and request.FILES['document']:
        myfile = request.FILES['document']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        print(filename)
        #Update File table
        file = Fileinfo()
        file.position = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'media')
        file.position = file.position + filename
        print(file.position)
        if len(filename.split('.')) > 1:
            file.format = filename.split('.')[1]
        else:
            file.format = ''
        file.uid = uid
        file.save()
       #Update Content table
        content = Content.objects.get(id=contentid)
        content.teafileid=file.id
        content.save()
        path='/index_tea/'+str(uid)
    return redirect(path)




