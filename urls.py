from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.registration, name='registration'),
    path('horoscope/<str:horo>/', views.horoscope, name='horoscope'),
    path('news/<int:news_id>/', views.news, name='news'),
    path('message/', views.message, name='message'),
    path('message_list/', views.message_list, name='message_list'),
    path('create_room/<int:user_id>/', views.create_room, name='create_room'),
    path('dialog/<int:room_id>/', views.dialog, name='dialog'),
    path('specialist_conversations/', views.specialist_conversations, name='specialist_conversations'),
  ]