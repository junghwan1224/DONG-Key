from django.urls import path
from . import views

app_name = 'club'

urlpatterns = [
    path('create/', views.create_club, name='create_club'),
    path('read_admin_club/<str:club>/', views.read_admin_club, name='read_admin_club'),
    path('read_non_admin_club/<str:club>/', views.read_non_admin_club, name='read_non_admin_club'),
    path('apply/<str:club>/', views.apply_club, name='apply_club'),
    path('admit/<str:club>/<int:pk>/', views.admit, name='admit'),
    path('create/club/rule/<str:club>/', views.create_club_rule, name='create_club_rule'),
    path('update/club/rule/<str:club>/<int:rule_pk>/', views.update_club_rule, name='update_club_rule'),
    path('delete/club/rule/<str:club>/<int:rule_pk>/', views.delete_club_rule, name='delete_club_rule'),
]
