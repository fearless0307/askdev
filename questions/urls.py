from django.urls import path, include
from questions import views, views_tag

urlpatterns = [
    path('', views.questions_home, name='questions-home'),
    path('questions/', views.questions_home, name='questions-home'),
    path('questions/<int:pk>/', views.question_detail, name="questions-detail"),
    path('questions/add/', views.question_create, name="questions-add"),
    path('questions/<int:pk>/edit/', views.question_update, name="questions-edit"),
    path('questions/<int:pk>/delete/', views.question_delete, name="questions-delete"),

    path('tags/',views_tag.tag_home, name = 'tags-home'),
    # path('tags/<str:name>/',views_tag.tag_detail, name='tags-detail'),
    path('tags/<str:name>/questions/',views_tag.tag_question, name='tags-questions'),
    path('tags/<str:name>/stories/',views_tag.tag_story, name='tags-stories'),

    path('testing/',views_tag.testing, name = 'testing'),   #can delete

]
