# Form Builder

A dynamic Django-based form builder application that allows users to create custom forms with various question types, conditional logic, and automatic calculations.

## 🌟 Features

- Create custom forms with multiple question types
- Support for conditional questions
- Automatic calculations for numeric responses
- Response collection and analysis
- User-friendly interface
- Real-time form preview
- Export response data

## 🚀 Question Types Supported

- Text input
- Integer/Numeric input
- Multiple Choice (Single answer)
- Multiple Choice (Multiple answers)
- Conditional questions based on previous answers

## 💻 Tech Stack

- Python 3.8+
- Django 5.1.5
- SQLite (default database)
- HTML/CSS/JavaScript
- Django Template Language

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## ⚙️ Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/form-builder.git
cd form-builder
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Create superuser (admin)
```bash
python manage.py createsuperuser
```

6. Start the development server
```bash
python manage.py runserver
```

## 📁 Project Structure

```
formbuilder/
├── formbuilder/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── forms/                # Main application
│   ├── models.py         # Database models
│   ├── views.py         # View logic
│   ├── urls.py          # URL routing
│   ├── admin.py         # Admin interface
│   └── templates/       # HTML templates
├── static/              # Static files
├── manage.py
└── requirements.txt
```

## 🔧 Database Models

### Form
```python
class Form(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
```

### Question
```python
class Question(models.Model):
    QUESTION_TYPES = [
        ('text', 'Text'),
        ('integer', 'Integer'),
        ('mcq_single', 'Multiple Choice (Single)'),
        ('mcq_multiple', 'Multiple Choice (Multiple)')
    ]
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    question_type = models.CharField(max_length=50, choices=QUESTION_TYPES)
    required = models.BooleanField(default=False)
    include_in_calculations = models.BooleanField(default=False)
```

### Response
```python
class Response(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    respondent_name = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)
```

## 🎯 Usage Guide

### Creating a Form

1. Access the home page at `http://localhost:8000`
2. Click "Create New Form"
3. Fill in form details:
   - Title (required)
   - Description (optional)
4. Add questions:
   - Question text
   - Question type
   - Required/Optional setting
   - For MCQ: Add options
   - For numeric: Set calculation inclusion
5. Save the form

### Managing Forms

- View all forms on the home page
- Click form title to view details
- Use "Delete" button to remove forms
- Access responses through "View Responses" button

### Submitting Responses

1. Access form through provided URL
2. Fill in respondent information
3. Answer questions:
   - Red asterisk (*) indicates required questions
   - Multiple choice: Select option(s)
   - Text: Enter free-form text
   - Number: Enter numeric values
4. Click "Submit" to save response

### Viewing Responses

1. Access form dashboard
2. Click "View Responses"
3. View:
   - Individual responses
   - Calculated totals
   - Averages for numeric questions
   - Response statistics



## 📱 Key URLs

- Home: `/`
- Create Form: `/create/`
- View Form: `/form/<form_id>/`
- Submit Response: `/form/<form_id>/submit/`
- View Responses: `/form/<form_id>/responses/`
- Admin Panel: `/admin/`



## 💡 Best Practices

1. Form Creation:
   - Use clear, concise questions
   - Group related questions
   - Test conditional logic
   - Verify calculations

2. Response Collection:
   - Regular data backup
   - Monitor response patterns
   - Review calculation accuracy
   - Export data periodically

## 🔍 Troubleshooting

Common Issues:
1. Installation Problems
   - Verify Python version
   - Check virtual environment
   - Confirm dependencies

2. Database Issues
   - Run migrations
   - Check permissions
   - Verify configuration

3. Form Submission Issues
   - Check required fields
   - Verify input formats
   - Test conditional logic




Made by Usha