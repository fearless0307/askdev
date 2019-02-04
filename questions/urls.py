from django.urls import path, include
from questions import views
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    
    path('api/questions/', views.Question_class.as_view(),name='questions'),
    path('api/questions/<int:pk>/', views.Question_Detail_class.as_view(), name="question-detail"),
    path('',include('users.urls')), 
]