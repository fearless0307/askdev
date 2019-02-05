from django.urls import path
from users import views
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
   
    path('users/', views.User_class.as_view(),name='users'),
    path('users/<int:pk>/', views.User_Detail_class.as_view(), name="user-detail"),

]