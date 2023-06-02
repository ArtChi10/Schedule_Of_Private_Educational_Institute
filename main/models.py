from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
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
    initials = models.CharField(null=True, blank=True, max_length=3)

    def __str__(self):
        return self.initials

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Student(models.Model):
    user = models.OneToOneField(AdvUser, on_delete=models.CASCADE)
    study_group = models.ForeignKey(StudyGroup, on_delete=models.PROTECT, verbose_name="Учебная группа")

    def __str__(self):
        return self.user.last_name
    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

