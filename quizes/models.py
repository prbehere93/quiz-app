from django.db import models
# Create your models here.
DIFFICULTY=(
    ('easy','easy'),
    ('medium','medium'),
    ('hard','hard')
)
class Quiz(models.Model):
    name=models.CharField(max_length=100)
    topic=models.CharField(max_length=100)
    number_of_questions=models.PositiveIntegerField()
    time=models.PositiveIntegerField(help_text="duration of the quiz in minutes")
    passing_score=models.PositiveIntegerField(help_text="score to pass")
    topic=models.CharField(max_length=100,choices=DIFFICULTY)
    created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name}_{self.topic}'
    
    def get_questions(self):
        return f'{self.question_set.all()[:self.number_of_questions]}'
    
    class Meta:
        verbose_name_plural='Quizes'
    
    
    
    