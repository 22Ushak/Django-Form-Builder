from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_form, name='create_form'),
    path('form/<int:form_id>/', views.view_form, name='view_form'),
    path('form/<int:form_id>/delete/', views.delete_form, name='delete_form'),  # Add this
    path('form/<int:form_id>/submit/', views.submit_response, name='submit_response'),
    path('form/<int:form_id>/responses/', views.view_responses, name='view_responses'),
    
    
]