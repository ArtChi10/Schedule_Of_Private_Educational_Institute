from django import forms
from .models import Lesson, Classroom
from main.models import LessonName, StudyGroup, Teacher
from django.forms import ModelForm, TextInput, DateInput, ModelChoiceField, Select, SelectDateWidget, ChoiceField
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget


class LessonForm(ModelForm):
    lesson_name = ModelChoiceField(queryset=LessonName.objects.all(), to_field_name='lesson_name')
    name_of_group = ModelChoiceField(queryset=StudyGroup.objects.all(), to_field_name='name_of_group')
    classroom = ModelChoiceField(queryset=Classroom.objects.all(), to_field_name='number_of_classroom')
    teacher = ModelChoiceField(queryset=Teacher.objects.all(), to_field_name='initials')
    number_of_slot_CHOISES = (("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6"), ("7", "7"),
                              ("8", "8"), ("9", "9"))
    number_of_slot = ChoiceField(choices=number_of_slot_CHOISES)
    date_of_lesson = DateField(widget=DateInput(attrs={
        'class': 'form-control',
        'placeholder': 'Дата урока',
    }))

    class Meta:
        model = Lesson
        fields = ['lesson_name', 'name_of_group', 'classroom', 'teacher', 'date_of_lesson', 'number_of_slot']
        widgets = {
            "lesson_name": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Предмет',
            }),
            "name_of_group": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Учебная группа',
            }),
            "classroom": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Аудитория',
            }),
            "teacher": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Преподаватель',
            }),
            "number_of_slot": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер занятия по распорядку'
            }),

        }
