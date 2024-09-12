from django.urls import path
from .views import login_view, register_view, ForgotPassword, PasswordResetSent, ResetPassword
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('forgot-password/', ForgotPassword, name='forgot-password'),
    path('password-reset-sent/<str:reset_id>/',PasswordResetSent, name='password-reset-sent'),
    path('reset-password/<str:reset_id>/', ResetPassword, name='reset-password'),
        
]