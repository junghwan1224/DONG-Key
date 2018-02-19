from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    path('<int:pk>/accounting/', views.club_accounting, name='club_accounting'),
]
