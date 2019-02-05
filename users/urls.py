from django.urls import path, include
from users import views
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
   
    # path('', include('questions.urls')),
    path('api/users/', views.User_class.as_view(),name='users'),
    path('api/users/<int:pk>/', views.User_Detail_class.as_view(), name="user-detail"),
    path('api/users/<int:pk>/questions',views.User_Question_Detail_class.as_view() ),
]