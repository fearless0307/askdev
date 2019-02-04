from django.urls import path
from users import views
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    
    # path('', views.home,name='home'),
    path('users/', views.User_class.as_view(),name='users'),
    path('users/<int:pk>/', views.User_Detail_class.as_view(), name="user-detail"),
    # path('deliveries/', views.Deliveries_class.as_view(),name='deliveries'),
    # path('deliveries/<int:pk>', views.Delivery_Detail_class.as_view(),name='deliveries-detail'),
    
]