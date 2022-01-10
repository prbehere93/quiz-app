from django.contrib import admin
from .models import Question, Answer

# Register your models here.

#using tabular inline
class AnswerInline(admin.TabularInline):
    model=Answer
    
class QuestionAdmin(admin.ModelAdmin):
    inlines=[AnswerInline]
    
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)