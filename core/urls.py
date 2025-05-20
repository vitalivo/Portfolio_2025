from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('certificates/', views.certificates, name='certificates'),
    path('contact/', views.contact, name='contact'),
    path('api/project/<int:pk>/', views.project_preview_api, name='project_preview_api'),
]