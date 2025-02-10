from django.shortcuts import render, get_object_or_404, redirect
from .models import Form, Question, Response, Answer

def home(request):
    forms = Form.objects.all()
    return render(request, 'forms/home.html', {'forms': forms})

def create_form(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        form = Form.objects.create(title=title, description=description)

        # Get all question data (use getlist to handle multiple values)
        question_texts = request.POST.getlist('question_text')
        question_types = request.POST.getlist('question_type')
        required_fields = request.POST.getlist('required')
        options_list = request.POST.getlist('options')
        parent_indices = request.POST.getlist('parent_question')
        trigger_answers = request.POST.getlist('trigger_answer')

        # Create all questions first
        questions = []
        for i in range(len(question_texts)):
            # Safely get values with defaults
            question_text = question_texts[i] if i < len(question_texts) else ''
            question_type = question_types[i] if i < len(question_types) else 'text'
            required = required_fields[i] == 'on' if i < len(required_fields) else False
            options = options_list[i] if i < len(options_list) else ''

            question = Question.objects.create(
                form=form,
                text=question_text,
                question_type=question_type,
                required=required,
                options=options,
            )
            questions.append(question)

        # Link parent questions (if any)
        for i in range(len(questions)):
            # Safely get parent index and trigger answer
            parent_index_str = parent_indices[i] if i < len(parent_indices) else ''
            trigger_answer = trigger_answers[i] if i < len(trigger_answers) else ''

            if parent_index_str.isdigit():
                parent_index = int(parent_index_str)
                if parent_index < len(questions):
                    questions[i].parent_question = questions[parent_index]
                    questions[i].trigger_answer = trigger_answer
                    questions[i].save()

        return redirect('view_form', form_id=form.id)
    return render(request, 'forms/create_form.html')
def view_form(request, form_id):
    form = get_object_or_404(Form, id=form_id)
    return render(request, 'forms/view_form.html', {'form': form})

def submit_response(request, form_id):
    form = get_object_or_404(Form, id=form_id)
    if request.method == 'POST':
        response = Response.objects.create(form=form, respondent_name=request.POST.get('respondent_name'))
        for question in form.questions.all():
            answer_text = request.POST.get(f'question_{question.id}')
            if question.question_type.startswith('mcq'):
                answer_text = ', '.join(request.POST.getlist(f'question_{question.id}'))
            Answer.objects.create(response=response, question=question, answer_text=answer_text)
        return redirect('home')
    return render(request, 'forms/submit_response.html', {'form': form})

def view_responses(request, form_id):
    form = get_object_or_404(Form, id=form_id)
    responses = form.responses.all()
    return render(request, 'forms/view_responses.html', {'form': form, 'responses': responses})

def delete_form(request, form_id):
    if request.method == 'POST':
        form = get_object_or_404(Form, id=form_id)
        form.delete()
    return redirect('home')