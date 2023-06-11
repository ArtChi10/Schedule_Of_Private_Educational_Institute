from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from datetime import datetime, date
from .utilities import get_timestamp_path

# Create your models here.


class AdvUser(AbstractUser):
    patronymic = models.CharField(max_length=64, null=True, blank=True, verbose_name='Отчество')
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(unique=True, help_text="Начни с +7", verbose_name='Номер телефона')
    avatar = models.ImageField(blank=True, upload_to='get_timestamp_path', verbose_name='Аватар пользователя')
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошел активацию?')
    send_messages = models.BooleanField(default=True, verbose_name='Слать оповещения о новых комментариях?')

    def get_full_name(self):
        full_name = f"{self.last_name} {self.first_name}"
        if self.patronymic:
            full_name += f" {self.patronymic}"
        return full_name

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
    lesson_name = models.CharField(max_length=50, verbose_name='Учебный предмет', default="Практика")

    def __str__(self):
        return self.lesson_name

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

    def get_lesson_names(self):
        return self.lesson_names.all()

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
