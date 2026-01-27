from django.urls import path
from . import views

urlpatterns = [
    path('auth-test/', views.AuthTestView.as_view(), name='auth-test'),

    path('boxes/', views.BoxListCreateView.as_view()),
    path('boxes/<int:pk>/', views.BoxRetrieveUpdateDestroyView.as_view()),
    
    path('boxes/<int:box_id>/threads/', views.ThreadListCreateView.as_view({"get":"list", "post":"create"})),
    path('boxes/<int:box_id>/threads/<int:thread_id>/', views.SendMessageView.as_view()),

]