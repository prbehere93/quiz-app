from django.http import JsonResponse
from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView, DetailView
# Create your views here.

class QuizListView(ListView):
    model=Quiz
    template_name='quizes/main.html' #check this out 
    
class QuizDetailView(DetailView):
    model=Quiz
    template_name='quizes/quiz.html'

def quiz_data_view(request,pk):
    quiz=Quiz.objects.get(pk=pk)
    questions=[]
    for q in quiz.get_questions():
        ans=[]
        for a in q.get_answers():
            ans.append(a.text)
        questions.append({str(q):ans})
    return JsonResponse({
        'data':questions,
        'time':quiz.time
    })