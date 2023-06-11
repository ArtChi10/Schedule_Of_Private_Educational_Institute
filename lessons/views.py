from django.db.models import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LessonForm
from .models import Lesson, Classroom
from main.models import Teacher, Course, StudyGroup, LessonName
from django.http import JsonResponse
from datetime import datetime, timedelta


def LessonsHome(request):
    list_of_study_group = StudyGroup.objects.all()
    list_of_course = Course.objects.all()
    context = {
        'list_of_study_group': list_of_study_group,
        'list_of_course': list_of_course,
    }
    return render(request, 'lessons/lesson_home.html', context)


def LessonCreate(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lessons:lesson_home")
    else:
        form = LessonForm()

    data = {
        'form': form
    }

    return render(request, 'lessons/lesson_create.html', data)


def get_teachers(request):
    lesson_name_id = request.GET.get('lesson_name')
    teachers: QuerySet[Teacher] = Teacher.objects.filter(lesson_names__lesson_name=lesson_name_id)
    teachers_data = [{'id': teacher.id, 'initials': teacher.initials} for teacher in teachers]
    data = {'teachers': teachers_data}
    return JsonResponse(data)


def group_schedule(request, group_id):
    group = get_object_or_404(StudyGroup, id=group_id)
    now_date = datetime.date(datetime.now())
    n_now_date = now_date.strftime('%Y-%m-%d')
    if request.GET.get('date'):
        date = request.GET.get('date')
        date = datetime.strptime(date, '%Y-%m-%d')
    else:
        date = now_date
    prev_date = (date - timedelta(days=7))
    prev_date = prev_date.strftime('%Y-%m-%d')
    next_date = date + timedelta(days=7)
    next_date = next_date.strftime('%Y-%m-%d')
    week_days = get_week_days(date)
    lessons_for_days = {}
    for i in week_days:
        lessons_for_days[i] = Lesson.objects.filter(name_of_group__id=group_id, date_of_lesson=i).order_by('number_of_slot')
    return render(request, 'lessons/group_schedule.html', {'group': group, 'lessons_for_days': lessons_for_days,
                                                           'prev_date': prev_date, 'next_date': next_date, 'n_now_date': n_now_date})


def get_week_days(date):
    monday_of_week = date-timedelta(days=date.isoweekday()%7-1)
    week_days = ['']*6
    for i in range(6):
        week_days[i] = monday_of_week
        monday_of_week = monday_of_week+timedelta(days=1)
    return week_days


from django.core.exceptions import ValidationError

# Создаем экземпляр модели с неправильными данными
lesson = Lesson(
    lesson_name=LessonName.objects.get(lesson_name="Математический анализ"),
    name_of_group=StudyGroup.objects.get(name_of_group='22-05-м'),
    classroom=Classroom.objects.get(number_of_classroom='01'),
    teacher=Teacher.objects.get(initials="Голубев ПА"),
    date_of_lesson="2023-6-12",
    number_of_slot="1"
 )


