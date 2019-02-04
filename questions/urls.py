from django.urls import path
from questions import views


urlpatterns = [
    path('api/replies/',views.Reply_list.as_view()),
    path('api/replies/<int:pk>/',views.Reply_detail.as_view()),
    path('api/questionreaction/',views.QuestionReaction_list.as_view()),
    path('api/questionreaction/<int:pk>/',views.QuestionReaction_detail.as_view()),
    path('api/tags/',views.Tags_list.as_view()),
    path('api/tags/<int:pk>/',views.Tags_detail.as_view()),
]