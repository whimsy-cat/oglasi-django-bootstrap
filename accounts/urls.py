from django.urls import path
from . import views

urlpatterns = [
    path('registracija/', views.register, name="register"),
    path('prijava/', views.login, name="login"),
    path('odjava/', views.logout, name="logout"),
    path('aktivacija/<uidb64>/<token>', views.activate, name="activate"),

    path('zaboravljena-sifra/', views.forgot_password, name="forgot_password"),
    path('reset-sifre-validacija/<uidb64>/<token>', views.reset_password_validate, name="reset_password_valited"),
    path('reset-sifre/', views.reset_password, name="reset_password"),

    path('profil/<username>', views.user_profile, name="user_profile"),
]
