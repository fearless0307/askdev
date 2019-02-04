from django.urls import path, include
from questions import views
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    
    # path('', views.home,name='home'),
    path('api/questions/', views.Question_class.as_view(),name='questions'),
    path('api/questions/<int:pk>/', views.Question_Detail_class.as_view(), name="question-detail"),
    path('',include('users.urls')),
    # path('deliveries/', views.Deliveries_class.as_view(),name='deliveries'),
    # path('deliveries/<int:pk>', views.Delivery_Detail_class.as_view(),name='deliveries-detail'),
    
]