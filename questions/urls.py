from django.urls import path, include
from questions import views

urlpatterns = [
    path('', views.questions_home, name='questions-home'),
]
