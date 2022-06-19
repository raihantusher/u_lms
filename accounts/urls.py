from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    #path('dashboard/', views.dashboard, name='dashboard'),
    #path('', views.dashboard, name='dashboard'),

    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('reset-password/', views.reset_password, name='reset_password'),

    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),

]
