from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from datetime import datetime, date

# Create your models here.


class AdvUser(AbstractUser):
    patronymic = models.CharField(max_length=64, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(unique=True, help_text="Начни с +7")
    avatar = models.ImageField(upload_to='user_avatars', blank=True, null=True)
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошел активацию?')
    send_messages = models.BooleanField(default=True, verbose_name='Слать оповещения о новых комментариях?')

    class Meta(AbstractUser.Meta):
        pass


class Course(models.Model):
    name_of_course = models.CharField(verbose_name='Учебные курсы', max_length=20, default="")

    def __str__(self):
        return self.name_of_course

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class StudyGroup(models.Model):
    name_of_group = models.CharField(verbose_name="Учебные группы", max_length=15, default="")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default="1")

    def __str__(self):
        return self.name_of_group

    class Meta:
        verbose_name = 'Учебная группа'
        verbose_name_plural = 'Учебные группы'


class LessonName(models.Model):
    name = models.CharField(max_length=50, verbose_name='Учебный предмет', default="Практика")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учебный предмет'
        verbose_name_plural = 'Учебные предметы'


class Teacher(models.Model):
    user = models.OneToOneField(AdvUser, on_delete=models.CASCADE)
    lesson_names = models.ManyToManyField(LessonName)
    initials = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.initials

    def save(self, *args, **kwargs):
        self.initials = f"{self.user.last_name} {self.user.first_name[0]}{self.user.patronymic[0]}"
        super().save(*args, **kwargs)
    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Student(models.Model):
    user = models.OneToOneField(AdvUser, on_delete=models.CASCADE)
    study_group = models.ForeignKey(StudyGroup, on_delete=models.PROTECT, verbose_name="Учебная группа")

    def __str__(self):
        return self.user.last_name and self.user.first_name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


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
        count = Lesson.objects.filter(lesson_name=self.lesson_name, StudyGroup=self.name_of_group,
                                      classroom=self.classroom, teacher=self.teacher,
                                      date_of_lesson=self.date_of_lesson, number_of_slot=self.number_of_slot).count()
        if count > 0:
            raise ValidationError("Неправильно заполненное занятие")

    def get_absolute_url(self):
        return f'/lessons/{self.id}'


class HeadTeacher(models.Model):
    user = models.OneToOneField(AdvUser, on_delete=models.CASCADE)
    initials = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.initials

    def save(self, *args, **kwargs):
        self.initials = f"{self.user.last_name} {self.user.first_name[0]}{self.user.patronymic[0]}"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заведующий учебной частью'
        verbose_name_plural = "Заведующие учебной частью"
