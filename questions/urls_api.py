from django.urls import path
from questions import views_api as views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.all_api, name='all-api'),
    # question api
    path('questions/', views.Question_class.as_view(), name='questions'),
    path('questions/<int:pk>/', views.Question_Detail_class.as_view(),name="question-detail"),
    path('questions/<int:pk>/answers/', views.Answer_list.as_view(),name='question-answers'),
    path('questions/<int:qid>/answers/<int:pk>/', views.Answer_detail.as_view(),name='answer-detail'),
    # path('questions/<int:pk>/reactions/',views.QuestionReaction_list.as_view(),name='question-reactions'),
    # question reaction api
    # path('questionreactions/<int:pk>/', views.QuestionReaction_detail.as_view(),name="questionreaction-detail"),
    # reaction api
    path('reactions/', views.Reaction_list.as_view(),name='reactions'),
    path('reactions/<int:pk>/', views.Reaction_detail.as_view(),name="reaction-detail"),
    # question tag api
    # path('questions/<int:pk>/tags/', views.QuestionTag_list.as_view(),name='question-tags'),
    # path('questiontags/<int:pk>/', views.QuestionTag_detail.as_view(),name ='questiontag-detail'),
    # tag api
    path('tags/', views.Tags_list.as_view(),name ='tag'),
    path('tags/data/', views.Tags_data_list.as_view(),name ='tag-data'),
    path('tags/<str:name>/', views.Tags_detail.as_view(),name ='tag-detail'),
    path('tags/<str:name>/questions/', views.Tags_questions.as_view(),name ='tag-question-detail'),
    # reply api
    # path('replies/', views.Reply_list.as_view(),name='reply'),
    path('replies/<int:pk>/', views.Reply_detail.as_view(),name='reply-detail'),

    
]

urlpatterns = format_suffix_patterns(urlpatterns)
