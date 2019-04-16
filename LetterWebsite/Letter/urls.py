from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin
from Letter import views as user_views

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
    path('logout/', views.logout_view, name='logout_view'),
    path('request/', views.request, name='request'),
    path('login/', auth_views.LoginView.as_view(template_name='Letter/login.html'), name='login'),

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
