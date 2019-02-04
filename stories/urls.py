from django.urls import path
from . import views
from .views import StorylistView, StorydetailView

urlpatterns = [
    path('', StorylistView.as_view(), name='stories-home'),
    path('<int:pk>/', StorydetailView.as_view(), name='story-detail'),
]
