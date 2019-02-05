from django.urls import path, include
from questions import views
from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    path('api/questions/', views.Question_class.as_view(), name='questions'),
    path('api/questions/<int:pk>/', views.Question_Detail_class.as_view(), name="question-detail"),
    path('api/questions/<int:pk>/answer/', views.Answer_list.as_view(),name='question-answers'),
    path('api/questions/<int:qid>/answer/<int:pk>/', views.Answer_detail.as_view(),name='answer-detail'),
    path('api/questions/<int:pk>/questionreaction/', views.QuestionReaction_list.as_view(),name='question-reactions'),
    path('api/questionreaction/<int:pk>/', views.QuestionReaction_detail.as_view(),name="questionreaction-detail"),
    path('api/reactions/', views.Reaction_list.as_view(), name='reactions'),
    path('api/reactions/<int:pk>/', views.Reaction_detail.as_view(), name="reaction-detail"),
    path('api/questions/<int:pk>/questiontag/', views.QuestionTag_list.as_view(),name='question-tags'),
    path('api/questiontag/<int:pk>/', views.QuestionTag_detail.as_view()),
    path('api/tag/', views.Tags_list.as_view()),
    path('api/tag/<int:pk>/', views.Tags_detail.as_view()),
    path('api/reply/', views.Reply_list.as_view()),
    path('api/reply/<int:pk>/', views.Reply_detail.as_view()),

     
]

urlpatterns = format_suffix_patterns(urlpatterns)