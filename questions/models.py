from django.db import models
from quizes.models import Quiz

# Create your models here.
class Question(models.Model):
    text=models.CharField(max_length=200)
    quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return f"{self.text}"
    
    def get_answers(self):
        return self.answers.all() #using the related name from Answer model, answer_set normally without the related name
    
class Answer(models.Model):
    text=models.CharField(max_length=200)
    correct=models.BooleanField(default=False)
    question=models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'question: {self.question.text} answer: {self.text} correct: {self.correct}'
    