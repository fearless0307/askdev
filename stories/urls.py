from django.urls import path
from stories import views

urlpatterns = [
    path('stories/', views.stories_home, name='stories-home'),
    path('stories/<int:pk>/', views.stories_detail, name='stories-detail'),
    path('stories/add/', views.stories_create, name='stories-add'),
    path('stories/<int:pk>/edit/', views.stories_edit, name='stories-edit'),
    path('stories/<int:pk>/delete/', views.stories_delete,
         name='stories-delete'),
    path('stories/<int:pk>/<reaction>/',
         views.submit_reaction, name='stories-reaction'),

]
