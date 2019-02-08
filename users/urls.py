from django.urls import path, include
from django.contrib.auth import views as auth_views

from users import views as user_views
from questions import views_tag

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('user-profile/', user_views.display_user_profile, name='user-profile'),
    path('login/', auth_views.LoginView.as_view(
         template_name='users/login.html'),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(
         template_name='users/logout.html'),
         name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/password_reset_done.html'),
        name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
            template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
            template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    path('fav/', user_views.fav_questions, name='fav-questions'),
    path('myposts/', user_views.my_posts, name='my-posts'),
]
