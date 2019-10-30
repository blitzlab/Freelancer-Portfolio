from django.urls import path, include
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.FreelanceView.as_view(), name = 'index'),
    path('send-email', views.send_email, name = 'email')
]
