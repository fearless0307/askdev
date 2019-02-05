from django.urls import path, include
from questions import views
# from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.questions_home, name='questions-home'),
    path('api/reply/', views.Reply_list.as_view()),
    path('api/reply/<int:pk>/', views.Reply_detail.as_view()),
    path('api/questionreaction/', views.QuestionReaction_list.as_view()),
    path('api/questionreaction/<int:pk>/',
         views.QuestionReaction_detail.as_view()),
    path('api/tag/', views.Tags_list.as_view()),
    path('api/tag/<int:pk>/', views.Tags_detail.as_view()),
    path('api/questiontag/', views.QuestionTag_list.as_view()),
    path('api/questiontag/<int:pk>/', views.QuestionTag_detail.as_view()),
    path('api/answer/', views.Answer_list.as_view()),
    path('api/answer/<int:pk>/', views.Answer_detail.as_view()),

    path('api/questions/', views.Question_class.as_view(), name='questions'),
    path('api/questions/<int:pk>/', views.Question_Detail_class.as_view(),
         name="question-detail"),
    path('', include('users.urls')),
]
