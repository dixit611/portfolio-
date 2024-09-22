from django.urls import path
from . import views
# from .views import test_email
from .views import register
from .views import login_page
from .views import logout_view


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
    path('certifications/', views.certifications, name='certifications'),
    path('certification/<int:id>/', views.certification_detail_view, name='certification_detail'),

    path('send-email/', views.send_email, name='send_email'),

    path('login_page/', login_page, name='login_page'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
]
