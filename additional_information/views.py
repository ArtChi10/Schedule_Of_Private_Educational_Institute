from django.shortcuts import render, redirect
from .forms import QuestionsForm  # Подключаем форму вопросов
from .models import Advertisement, Questions  # Подключаем модель объявлений
from django.contrib.auth.decorators import login_required


@login_required
def QuestionCreate(request):
    error = ""
    if request.method == 'POST':
        form = QuestionsForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.FIO = request.user.get_full_name()
            question.email = request.user.email
            question.NumberPhone = request.user.phone
            question.save()
            return redirect("main:profile")
        else:
            error = 'Форма была заполнена некорректно'    # описываем ошибку
    else:
        form = QuestionsForm(initial={
            'FIO': request.user.get_full_name(),
            'email': request.user.email,
            'NumberPhone': request.user.phone
        })
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'additional_information/question_create.html', data)


def QuestionList(request):
    questions = Questions.objects.order_by('-published')
    return render(request, 'additional_information/question_list.html', {'questions': questions})
