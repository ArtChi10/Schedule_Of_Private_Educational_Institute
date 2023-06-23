from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, UpdateView, DeleteView

from main.views import head_teacher_required
from .forms import QuestionsForm, AdvertisementForm  # Подключаем форму вопросов
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
            error = 'Форма была заполнена некорректно'  # описываем ошибку
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


@login_required()
def AdvertisementList(request):
    advs = Advertisement.objects.order_by('-published')  # создаем список объявлений, фильтруя по дате объявления,
    # самое позднее - выше всех
    return render(request, 'additional_information/main.html', {'advs': advs})


@head_teacher_required
def CreateAdvertisement(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("additional_information:ad_workplace")
    else:
        form = AdvertisementForm()

    return render(request, 'additional_information/ad_create.html', {'form': form})


@head_teacher_required
def AdvertisementWorkPlace(request):
    advs = Advertisement.objects.order_by('-published')
    return render(request, 'additional_information/ad_workplace.html', {'advs': advs})


class AdvDetailView(DetailView):
    model = Advertisement
    template_name = 'additional_information/details_view.html'
    context_object_name = 'Advertisement'


def AdvEditView(request, pk):
    advertisement = get_object_or_404(Advertisement, pk=pk)
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, instance=advertisement)
        if form.is_valid():
            form.save()
            return redirect('additional_information:ad_workplace')
    else:
        form = AdvertisementForm(instance=advertisement, initial={'title': advertisement.title, 'content': advertisement.content})
    return render(request, 'additional_information/details_view.html', {'form': form, 'advertisement': advertisement})


class AdvDeleteView(DeleteView):
    model = Advertisement
    success_url = reverse_lazy('additional_information:ad_workplace')  # URL, на который перенаправлять после успешного удаления
    template_name = 'additional_information/ad_delete.html'



