from django.urls import path
from . import views

app_name = 'recruiting'

urlpatterns = [
    path('<int:club_pk>/', views.admin_resume_list, name='admin_resume_list'),
    path('<int:club_pk>/applicant_list', views.applicant_resume_list, name='applicant_resume_list'),
    path('<int:club_pk>/create_admin', views.create_admin_resume, name='create_admin_resume'),
    path('<int:club_pk>/<int:resume_pk>/read_admin', views.read_admin_resume, name='read_admin_resume'),
    path('<int:club_pk>/<int:resume_pk>/create_question/', views.create_question, name='create_question'),
    path('<int:club_pk>/<int:resume_pk>/create_applicant/', views.create_applicant_resume,
         name='create_applicant_resume'),
    path('<int:club_pk>/<int:resume_pk>/read_applicant', views.read_applicant_resume,
         name='read_applicant_resume')

]
