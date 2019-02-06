from django.urls import path
from questions import views_api as views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # question api
    path('questions/', views.Question_class.as_view(),
         name='questions'),
    path('questions/<int:pk>/', views.Question_Detail_class.as_view(),
         name="question-detail"),
    path('questions/<int:pk>/answer/', views.Answer_list.as_view(),
         name='question-answers'),
    path('questions/<int:qid>/answer/<int:pk>/', views.Answer_detail.as_view(),
         name='answer-detail'),
    path('questions/<int:pk>/questionreaction/',
         views.QuestionReaction_list.as_view(),
         name='question-reactions'),
    # question reaction api
    path('questionreaction/<int:pk>/', views.QuestionReaction_detail.as_view(),
         name="questionreaction-detail"),
    # reaction api
    path('reactions/', views.Reaction_list.as_view(),
         name='reactions'),
    path('reactions/<int:pk>/', views.Reaction_detail.as_view(),
         name="reaction-detail"),
    # question tag api
    path('questions/<int:pk>/questiontag/', views.QuestionTag_list.as_view(),
         name='question-tags'),
    path('questiontag/<int:pk>/', views.QuestionTag_detail.as_view()),
    # tag api
    path('tag/', views.Tags_list.as_view()),
    path('tag/<int:pk>/', views.Tags_detail.as_view(), name="tag-detail"),
    # reply api
    path('reply/', views.Reply_list.as_view()),
    path('reply/<int:pk>/', views.Reply_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
