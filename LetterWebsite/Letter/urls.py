from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib import admin
from Letter import views as user_views

from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('signin/', views.register, name='register'),
    path('upload/', views.upload, name='upload'),
    path('schedule/', views.schedule, name='schedule'),
    path('letter/', views.letter, name='letter'),
    path('logout/', auth_views.LoginView.as_view(template_name='Letter/logout.html'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='Letter/login.html'), name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
