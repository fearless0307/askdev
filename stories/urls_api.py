from django.urls import path
from stories import views_api as views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # story api
    path('stories/', views.Story_list.as_view(), name="story-list"),
    path('stories/<int:pk>/', views.Story_detail.as_view(), name="story-detail"),
    path('tags/<str:name>/stories/', views.Tags_stories.as_view(),name ='tag-story-detail'),
    # story tag api
#     path('storytags/', views.StoryTag_list.as_view()),
#     path('storytags/<int:pk>/', views.StoryTag_detail.as_view()),
    # story reaction api
#     path('stories/<int:pk1>/reactions/',
#          views.StoryReaction_list.as_view()),
#     path('stories/<int:pk1>/reactions/<int:pk2>',
#          views.StoryReaction_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
