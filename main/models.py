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
class StudyGroup(models.Model):
    name_of_group = models.CharField(verbose_name="Учебные группы", max_length=15, default="")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default="1")
    def __str__(self):
        return self.name_of_group

