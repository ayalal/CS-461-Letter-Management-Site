from django.urls import path
from django.urls import  re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from Letter import views as user_views

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register/',views.register),
    path('register/register_check/',views.registerCheck),
    path('check_login/',views.checkLogin,name='checkLogin'),
    path('index_stu/',views.initStuIndex,name='initStuIndex'),
    path('search_teacher/<int:sid>/',views.searchTeacher),
    path('search_by_department/',views.searchByDepartment),
    path('upload/<int:uid>/',auth_views.LoginView.as_view(template_name='Letter/upload.html'),name='upload'),
    path('upload/<int:uid>/file/', views.upload),
    path('new_request/<int:uid>/',views.makeRequest),
    path('new_request/<int:uid>/submit/',views.submitRequest),
    path('index_tea/<int:uid>/',views.initTeacher,name='initTeaIndex'),
    path('index_tea/<int:uid>/<int:contentid>/feedback/',auth_views.LoginView.as_view(template_name='Letter/feedback.html')),
    path('index_tea/<int:uid>/<int:contentid>/upload/',auth_views.LoginView.as_view(template_name='Letter/upload_tea.html')),
    path('index_tea/<int:uid>/<int:contentid>/feedback/submit/',views.feedback),
    path('index_tea/<int:uid>/<int:contentid>/upload/submit/',views.uploadTeacherFile),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
