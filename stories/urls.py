from django.urls import path
from stories import views

urlpatterns = [
    path('stories/', views.stories_home, name='stories-home'),
    path('stories/<int:pk>/', views.StorydetailView.as_view(),
         name='story-detail'),
    path('stories/create/', views.StorycreateView.as_view(),
         name='story-create'),
    path('stories/<int:pk>/update/', views.StoryupdateView.as_view(),
         name='story-update'),
    path('stories/<int:pk>/delete/', views.StorydeleteView.as_view(),
         name='story-delete'),
]
