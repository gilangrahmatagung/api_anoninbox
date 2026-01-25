from django.urls import path
from . import views

urlpatterns = [
    path('auth-test/', views.AuthTestView.as_view(), name='auth-test'),

    path('boxes/', views.BoxListCreateView.as_view(), name="box"),
    path('boxes/<int:box_id>/', views.BoxRetrieveUpdateDestroyView.as_view(), name="box"),
    
    path('boxes/<int:box_id>/threads/', views.ThreadAndMessagesView.as_view(), name="threads-in-box"),
    path('boxes/<int:box_id>/threads/<int:thread_id>/', views.SendMessageView.as_view(), name="send-message"),

    path('start-thread/', views.StartThreadView.as_view(), name="start-thread"),


    # mending pake URL atau body untuk ambil field? keknya URL

]