from django.urls import path
from . import views

urlpatterns = [
    path('auth-test/', views.AuthTestView.as_view(), name='auth test')
]