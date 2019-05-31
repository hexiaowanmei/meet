from django.urls import path
from homepage import views


urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    # path('register/', views.register, name='register'),
    # path('indexs/', views.indexs, name='indexs'),
    path('meet_count/', views.meet_count, name='meet_count'),
    path('screen/', views.screen, name='screen'),
    path('slide/', views.slide, name='slide'),
    path('last_user/', views.last_user, name='last_user'),
    path('meets_site/', views.meets_site, name='meets_site'),
    path('user_friend/', views.user_friend, name='user_friend'),
]