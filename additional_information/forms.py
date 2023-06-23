from django.forms import ModelForm, TextInput, Textarea, EmailInput #Подключаем модули для ввода данных
from .models import Questions, Advertisement # подключаем модель Questuons приложения main
from main.models import AdvUser


class QuestionsForm(ModelForm):   # Создаем Форму вопроса
    class Meta:
        model = Questions  # указываем какую модель используем
        fields = ('topic', 'text', 'FIO', 'email', 'NumberPhone')   # сообщаем поля формы

        widgets = {     # Элемент ввода (описываем в каком виде будем получать данные
            'topic': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема вопроса'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст вопроса'
            }),
            'FIO': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ФИО автора'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'e-mail'
            }),
            'NumberPhone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            })
        }


class AdvertisementForm(ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'content']
        labels = {
            'title': 'Тема',
            'content': 'Содержание'
        }
        widgets = {
            'content': Textarea(attrs={'rows': 4})  # Настройка виджета для текстового поля "content"
        }
