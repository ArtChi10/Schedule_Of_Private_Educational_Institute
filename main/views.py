from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import AdvUser, Teacher, Student
from .forms import ChangeUserInfoForm, RegisterUserForm
from django.contrib.auth.views import PasswordChangeView
from .models import HeadTeacher
from django.core.signing import BadSignature
from .utilities import signer
from django.views.generic.edit import DeleteView
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CourseForm
from .models import Course
from .models import StudyGroup
from django.db.models import Q


# Create your views here.
def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


def index(request):
    return render(request, 'main/index.html')


class ScheduleLoginView(LoginView):
    template_name = 'main/login.html'


class ScheduleLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'


@login_required
def profile(request):
    return render(request, 'main/profile.html')


def ProfileView(request, pk):
    user_profile = get_object_or_404(AdvUser, pk=pk)
    return render(request, 'main/profile_details.html', {'user_profile': user_profile})


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = AdvUser
    template_name = 'main/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('main:profile')
    success_message = 'Данные пользователя изменены'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class SchedulePasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    template_name = 'main/password_change.html'
    success_url = reverse_lazy('main:profile')
    success_message = 'Пароль пользователя изменен'


class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'main/register_done.html'


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = AdvUser
    template_name = 'main/delete_user.html'
    success_url = reverse_lazy('main:index')

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'Пользователь удален')
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'main/bad_signature.html')
    user = get_object_or_404(AdvUser, username=username)
    if user.is_activated:
        template = 'main/user_is_activated.html'
    else:
        template = 'main/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)


def head_teacher_required(view_func):
    decorated_view_func = user_passes_test(
        lambda user: user.is_authenticated and HeadTeacher.objects.filter(user=user).exists(),
        login_url='login',
    )(view_func)
    return decorated_view_func


def teacher_required(view_func):
    decorated_view_func = user_passes_test(
        lambda user: user.is_authenticated and Teacher.objects.filter(user=user).exists(),
        login_url='login',
    )(view_func)
    return decorated_view_func


def student_required(view_func):
    decorated_view_func = user_passes_test(
        lambda user: user.is_authenticated and Student.objects.filter(user=user).exists(),
        login_url='login',
    )(view_func)
    return decorated_view_func

@head_teacher_required
def head_check(request):
    return render(request, 'main/headcheck.html')


from django.shortcuts import render
from .models import AdvUser


def user_search_view(request):
    query = request.GET.get('query', '')
    role_query = request.GET.get('role', '')
    users = AdvUser.objects.all()

    if query:
        users = users.filter(first_name__icontains=query) | users.filter(last_name__icontains=query)
    if role_query:
        if role_query == 'student':
            users = users.filter(student__isnull=False)
        elif role_query == 'teacher':
            users = users.filter(teacher__isnull=False)
        elif role_query == 'head_teacher':
            users = users.filter(headteacher__isnull=False)
    context = {
        'query': query,
        'role_query': role_query,
        'users': users,
    }
    return render(request, 'main/user_search.html', context)


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:create_setting_up_controls')  # Перенаправление на список курсов
    else:
        form = CourseForm()
    return render(request, 'main/create_course.html', {'form': form})


def create_setting_up_controls(request):
    list_of_course = Course.objects.all()
    list_of_group = StudyGroup.objects.all()
    return render(request, 'main/create_setting_up_controls.html', {'list_of_course': list_of_course,
                                                                    'list_of_group': list_of_group})
