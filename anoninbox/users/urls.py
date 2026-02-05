from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('ask-verification/', views.AskUserVerificationView.as_view()),
    path('check-verification/', views.CheckUserVerificationView.as_view()),
    path('ask-password-reset/', views.AskPasswordResetView.as_view()),
    path('check-password-reset/', views.CheckPasswordResetView.as_view())
]