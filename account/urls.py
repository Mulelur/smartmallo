from django.urls import path
from django.contrib.auth import views as auth_views
from account import views as account_views
from .views import order_tracking, my_account, delivery, edit_profile

urlpatterns = [
    path('profile/', account_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete'),
    path('Track-order/', order_tracking, name='order_tracking'),
    path('my-account/', my_account, name='my_account'),
    path('shipping/', delivery, name='delivery'),
    path('profile-edit/', edit_profile, name='edit_profile'),
]