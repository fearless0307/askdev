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
    path('api/storyreaction/', views.StoryReaction_list.as_view()),
    path('api/storyreaction/<int:pk>', views.StoryReaction_detail.as_view()),
    path('', views.StorylistView.as_view(), name='stories-home'),
    path('<int:pk>/', views.StorydetailView.as_view(), name='story-detail'),
    path('create/', views.StorycreateView.as_view(), name='story-create'),
    path('<int:pk>/update/', views.StoryupdateView.as_view(), name='story-update'),
    path('<int:pk>/delete/', views.StorydeleteView.as_view(), name='story-delete'),

]


