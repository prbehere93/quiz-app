from django.urls import path
from .views import (
    QuizListView,
    QuizDetailView
    )
app_name='quizes'

urlpatterns = [
    path('',QuizListView.as_view(), name='quiz-list'),
    path('<pk>/',QuizDetailView.as_view(), name='quiz-detail'),
]
