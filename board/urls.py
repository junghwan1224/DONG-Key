from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('list/<int:club_pk>/', views.article_list, name='article_list'),
    path('ctg/<int:club_pk>/<int:ctg_pk>/', views.article_list, name='article_list_by_ctg'),
    path('create/<int:club_pk>', views.article_create, name='article_create'),
    path('<int:pk>/', views.article_detail, name='article_detail'),
    path('update/<int:pk>/', views.article_update, name='article_update'),
    path('delete/<int:pk>/', views.article_delete, name='article_delete'),
    path('like/<int:pk>/', views.article_like, name='article_like'),
    path('comment_like/<int:pk>/', views.comment_like, name='comment_like'),

]