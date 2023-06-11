from django.db import models
from main.models import StudyGroup, Teacher, LessonName
from django.core.exceptions import ValidationError


# Create your models here.
class Classroom(models.Model):
    number_of_classroom = models.CharField(max_length=5, verbose_name="Номер аудитории")

    def __str__(self):
        return self.number_of_classroom

    class Meta:
        verbose_name = 'Номер учебной аудитории'
        verbose_name_plural = 'Номера учебных аудиторий'


class Lesson(models.Model):
    lesson_name = models.ForeignKey(LessonName, on_delete=models.CASCADE, verbose_name='Предмет', null=True)
    name_of_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, verbose_name='Учебная группа', null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, null=True, verbose_name="Учебная аудитория")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Преподаватель', null=True)
    date_of_lesson = models.DateField('Дата урока')
    number_of_slot = models.IntegerField('Порядковый номер учебного занятия')
    info_for_lesson = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.lesson_name)

    def clean(self):
        # Проверяем, есть ли уже занятия для других групп в указанной аудитории и дате
        existing_lessons = Lesson.objects.filter(name_of_group=self.name_of_group,
                                                 date_of_lesson=self.date_of_lesson,
                                                 number_of_slot=self.number_of_slot)
        if existing_lessons.exists():
            raise ValidationError("У данной группы в это время есть уже занятие")
        existing_lessons = Lesson.objects.filter(teacher=self.teacher,
                                                 date_of_lesson=self.date_of_lesson,
                                                 number_of_slot=self.number_of_slot
                                                 )
        if existing_lessons.exists():
            raise ValidationError("У преподавателя в этот момент другое занятие")
        existing_lessons = Lesson.objects.filter(classroom=self.classroom,
                                                 date_of_lesson=self.date_of_lesson,
                                                 number_of_slot=self.number_of_slot
                                                 )
        if existing_lessons.exists():
            raise ValidationError("Данная аудитория в этот момент занята")

    def get_absolute_url(self):
        return f'/lessons/{self.id}'

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"

