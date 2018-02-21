from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('read_profile/', views.read_profile, name='read_profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
]
