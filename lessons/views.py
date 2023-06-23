from django.db.models import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView

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
        lessons_for_days[i] = Lesson.objects.filter(name_of_group__id=group_id,
                                                    date_of_lesson=i).order_by('number_of_slot')
    return render(request, 'lessons/group_schedule.html',
                  {'group': group, 'lessons_for_days': lessons_for_days,
                    'prev_date': prev_date, 'next_date': next_date, 'n_now_date': n_now_date})




def CourseSchedule(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    group = StudyGroup.objects.filter(course=course)
    print(group)
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
        lessons_for_days[i] = Lesson.objects.filter(name_of_group__course_id=course_id,
                                                    date_of_lesson=i).order_by('number_of_slot')
    return render(request, 'lessons/course_schedule.html', {'course': course, 'group': group,
                                                            'lessons_for_days': lessons_for_days,
                                                            'prev_date': prev_date, 'next_date': next_date,
                                                            'n_now_date': n_now_date})


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


def lesson_info(request):
    if request.method == 'GET':
        lesson_id = request.GET.get('lesson_id')
        lesson = get_object_or_404(Lesson, id=lesson_id)
        return render(request, 'lessons/lesson_info.html', {'lesson': lesson})


class LessonDeleteView(DeleteView):
    model = Lesson
    success_url = reverse_lazy('lessons:lesson_home')  # URL, на который перенаправлять после успешного удаления
    template_name = 'lessons/lesson_delete.html'


def LessonEditView(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    lesson.is_editing = True  # Изменяем значение флага на True
    lesson.save()
    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            lesson.is_editing = False  # Изменяем значение флага
            lesson.save()
            return redirect('lessons:lesson_home')
    else:
        form = LessonForm(instance=lesson, initial={
            'lesson_name': lesson.lesson_name,
            'name_of_group': lesson.name_of_group,
            'classroom': lesson.classroom,
            'teacher': lesson.teacher,
            'number_of_slot': lesson.number_of_slot,
            'date_of_lesson': lesson.date_of_lesson,
        })

    return render(request, 'lessons/lesson_details.html', {'form': form, 'lesson': lesson})


