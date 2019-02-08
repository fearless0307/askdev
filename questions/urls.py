from django.urls import path, include
from questions import views, views_tag

urlpatterns = [
     path('', views.questions_home, name='questions-home'),
    path('questions/', views.questions_home, name='questions-home'),
    path('questions/<int:pk>/', views.question_detail, name="question_detail"),
    path('questions/new/', views.question_create, name="question-create"),
    path('questions/<int:pk>/update/', views.question_update, name="question-update"),
    path('questions/<int:pk>/delete/', views.question_delete, name="question-delete"),
    path('tags/',views_tag.tag_home, name = 'tag-home'),
    path('tags/<str:pk>/',views_tag.tag_detail, name='tag-detail'),
    path('tags/answers/<str:pk>',views_tag.tag_answer, name='tag-answer'),
    path('testing/',views_tag.testing, name = 'testing'),   #can delete

]
