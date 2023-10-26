from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='user_login'),
    path('register/', views.UserRegister.as_view(), name='user_register'),
    path('check_OTP/', views.Check_User_OTP.as_view(), name='user_check_OTP_register'),
    path('logout_user/', views.user_Logout, name='logout'),
]