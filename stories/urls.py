from django.urls import path
from stories import views

urlpatterns = [
    path('', views.stories_home, name='stories-home'),
    path('api/story/', views.Story_list.as_view()),
    path('api/story/<int:pk>/', views.Story_detail.as_view()),
    path('api/storytags/', views.StoryTag_list.as_view()),
    path('api/storytags/<int:pk>/', views.StoryTag_detail.as_view()),
    path('api/story/<int:pk1>/storyreaction/', views.StoryReaction_list.as_view()),
    path('api/story/<int:pk1>/storyreaction/<int:pk2>', views.StoryReaction_detail.as_view()),
]

