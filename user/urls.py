from django.urls import path
from user import views
# from user.views import ForCodeView

urlpatterns = [

    path('register/', views.register, name='register'),  # 注册
    path('detail_user/', views.detail_user, name='detail_user'),  # 完善信息
    path('add_label/', views.add_label, name='add_label'),  # 兴趣标签
    path('send_message/', views.send_message, name='send_message'),  # 发送短信
    path('login/', views.login, name='login'),  # 登录
    path('reset_password/', views.reset_password, name='reset_password'),  # 重置密码
    path('index/', views.index, name='index'),  # 我的
]
