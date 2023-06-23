from django.urls import path
from . import views

app_name = 'lessons'
urlpatterns = [
     path('lesson_details/<int:pk>/', views.LessonEditView, name='lesson_details'),
     path('lesson_delete/<int:pk>/', views.LessonDeleteView.as_view(), name='lesson_delete'),
     path('lesson_info/', views.lesson_info, name='lesson_info'),
     path('course_shedule/<int:course_id>/', views.CourseSchedule, name='course_schedule'),
     path('group_schedule/<int:group_id>/', views.group_schedule, name='group_schedule'),
     path('lesson_home/', views.LessonsHome, name='lesson_home'),
     path('lesson_create/', views.LessonCreate, name='lesson_create'),
     path('lesson_create/get_teachers/', views.get_teachers, name='get_teachers'),
]