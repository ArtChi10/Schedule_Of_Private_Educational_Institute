from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from main.models import AdvUser

# Create your models here.


class Advertisement(models.Model):
    title = models.CharField(max_length=50, verbose_name="Тема")
    content = models.TextField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name_plural = 'Объявления'


class Questions(models.Model):
    topic = models.CharField(max_length=100, verbose_name="Тема")
    text = models.TextField(null=True, blank=True, verbose_name='Текст вопроса')
    FIO = models.CharField(max_length=100, verbose_name='ФИО')
    email = models.EmailField(max_length=100, verbose_name='e-mail')
    NumberPhone = PhoneNumberField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name_plural = "Вопросы"

