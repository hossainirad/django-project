from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from django.contrib.auth.views import (
        password_reset,
        password_reset_done,
        password_reset_confirm,
        password_reset_complete,
)

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_views, name='logout'),
    path('profile/', views.profile_view, name='profile_view'),
    # path('profile/edit/', views.EditProfile.as_view(), name='edit_profile'),
    path('profile/edit/', views.EditProfile.as_view(), name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('reset-password/', password_reset, {'template_name': 'reset_password.html'}, name='reset_password'),
    path('reset-password/done/', password_reset_done, name='password_reset_done'),
    path('reset-password/confirm/', password_reset_confirm, name='password_reset_confirm'),
    path('reset-password/complete/', password_reset_complete, name='password_reset_complete'),
]
