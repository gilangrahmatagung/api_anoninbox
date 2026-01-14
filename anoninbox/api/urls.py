from django.urls import path
from . import views

urlpatterns = [
    path('auth-test/', views.AuthTestView.as_view(), name='auth-test'),

    path('box/', views.BoxListCreateView.as_view(), name="box"),
    path('box/<int:pk>/', views.BoxRetrieveUpdateDestroyView.as_view(), name="box"),

    path('start-thread/', views.StartThreadView.as_view(), name="start-thread"),
    path('create-message/', views.CreateMessageView.as_view(), name="create-message"),
]