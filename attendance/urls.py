from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('<int:pk>/create_event/', views.create_event, name='create_event'),
    path('<int:pk>/event_list/', views.event_list, name='event_list'),
    path('<int:event_pk>/read_event/', views.read_event, name='read_event'),

]
