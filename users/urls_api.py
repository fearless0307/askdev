from django.urls import path, include
from users import views_api as views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('users/', views.User_class.as_view(), name='users'),
    path('users/<int:pk>/', views.User_Detail_class.as_view(),
         name="user-detail"),
    path('users/<int:pk>/questions/',
         views.User_Question_Detail_class.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
