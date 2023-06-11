from django.urls import path
from . import views

app_name = 'additional_information'
urlpatterns = [
     path('question_create/', views.QuestionCreate, name='question_create'),
     path('question_list/', views.QuestionList, name='question_list'),
]