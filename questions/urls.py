from django.urls import path, include
from questions import views, views_tag

urlpatterns = [
    path('', views.questions_home, name='questions-home'),

    path('tag/',views_tag.tag_home, name = 'tag-home'),
    path('tag/<int:pk>/',views_tag.tag_detail, name='tag-detail')
]
