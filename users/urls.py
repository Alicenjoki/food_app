from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('login/', Login, name='login'),
    path('register/', register, name='register'),
    path('logout/', Logout, name='logout'),
    path('profile/', profile, name='profile'),
    # path('change_password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html'), name='change_password'),
    # path('change_password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    path('change_password/', change_password, name='change_password'),
    path('change_password_done/', change_password_done, name='change_password_done' ),    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',email_template_name='registration/password_reset_email.html',subject_template_name='registration/password_reset_subject.txt',success_url='/password_reset_done/'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html',success_url='/password_reset_complete/'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]