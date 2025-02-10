from django.contrib import admin
from .models import Form, Question, Response, Answer

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'form', 'question_type', 'parent_question', 'trigger_answer')

admin.site.register(Form)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Response)
admin.site.register(Answer)