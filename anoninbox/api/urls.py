from django.urls import path
from . import views

urlpatterns = [
    path('auth-test/', views.AuthTestView.as_view(), name='auth test'),

    path('box/', views.BoxListCreateView.as_view()),
    path('box/<int:pk>/', views.BoxRetrieveUpdateDestroyView.as_view())
]