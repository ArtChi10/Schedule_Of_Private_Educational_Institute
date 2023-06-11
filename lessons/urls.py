from django.urls import path
from . import views

app_name = 'lessons'
urlpatterns = [
     path('group_schedule/<int:group_id>/', views.group_schedule, name='group_schedule'),
     path('lesson_home/', views.LessonsHome, name='lesson_home'),
     path('lesson_create/', views.LessonCreate, name='lesson_create'),
     path('lesson_create/get_teachers/', views.get_teachers, name='get_teachers'),
]