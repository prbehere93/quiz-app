from django.urls import path
from .views import (
    QuizListView,
    QuizDetailView,
    quiz_data_view
    )
app_name='quizes'

urlpatterns = [
    path('',QuizListView.as_view(), name='quiz-list'),
    path('<pk>/',QuizDetailView.as_view(), name='quiz-detail'),
    path('<pk>/data/',quiz_data_view, name='quiz-data-view'),
]
