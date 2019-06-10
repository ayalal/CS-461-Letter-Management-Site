from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin
from Letter import views as user_views
import django_cas_ng.views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
 #   path('professor/', views.professor, name='professor'),
    path('professor_profiles/<int:user_id>/', views.professor_profiles, name='professor_profiles'),
    path('student_profiles/<int:user_id>/', views.student_profiles, name='student_profiles'),
 #   path('upload/', views.upload, name='upload'),
    path('schedule/', views.schedule, name='schedule'),
    path('letter/', views.letter, name='letter'),
    path('register/', views.register, name='register'),
    path('signin/', views.register, name='register'),
#    path('preference/', views.get_preference, name='preference'),
    path('preferences/', views.set_preferences, name='preferences'),
 #   path('logout/', views.logout_view, name='logout_view'),
    path('request/', views.request, name='request'),
#    path('login/', auth_views.LoginView.as_view(template_name='Letter/login.html'), name='login'),
    path('login/', django_cas_ng.views.LoginView.as_view(), name='cas_ng_login'),
    path('logout/', django_cas_ng.views.LogoutView.as_view(), name='cas_ng_logout'),
    path('oldlogin/', auth_views.LoginView.as_view(template_name='Letter/login.html'), name='login'),
    path(r'^(?P<document_id>[0-9]+)/delete_file/$', views.delete_file, name='delete_file'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
