# Generated by Django 5.1.5 on 2025-02-08 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='options',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('text', 'Text'), ('integer', 'Integer'), ('mcq_single', 'Multiple Choice (Single Correct)'), ('mcq_multiple', 'Multiple Choice (Multiple Correct)')], max_length=50),
        ),
    ]
