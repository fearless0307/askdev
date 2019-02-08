from django.urls import path, include
from questions import views, views_tag


urlpatterns = [
    path('', views.questions_home, name='questions-home'),
    path('questions/', views.questions_home, name='questions-home'),
    path('questions/search/', views.questions_search, name='questions-search'),
    path('questions/<int:pk>/', views.question_detail,
         name="questions-detail"),

    path('questions/add/', views.question_create, name="questions-add"),
    path('answers/add/', views.answer_create, name="add-answer"),
    path('replies/add/', views.reply_create, name="add-reply"),

    path('questions/<int:pk>/reaction/add/<str:name>/',
         views.submit_reaction, name='questions-reaction'),

    path('questions/<int:pk>/edit/', views.question_update,
         name="questions-edit"),
    path('questions/<int:pk>/delete/',
         views.question_delete, name="questions-delete"),

    path('tags/', views_tag.tag_home, name='tags-home'),
    path('tags/<str:name>/questions/',
         views_tag.tag_question, name='tags-questions'),
    path('tags/<str:name>/stories/', views_tag.tag_story, name='tags-stories'),

    path('about/', views_tag.about, name='about'),
    path('testing/', views_tag.testing, name='testing'),  # can delete
    # path('tags/<str:name>/',views_tag.tag_detail, name='tags-detail'),

]
