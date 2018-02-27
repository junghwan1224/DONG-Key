from django.urls import path
from . import views

app_name = 'finance'

urlpatterns = [
    path('<int:pk>/accounting/', views.club_accounting, name='club_accounting'),
    path('<int:pk>/accounting/search_by_date/', views.search_by_date, name='search_by_date'),
]