from django.urls import path
from .views import index, other_page
from .views import ScheduleLoginView
from .views import profile, head_check
from .views import ScheduleLogoutView
from .views import ChangeUserInfoView
from .views import SchedulePasswordChangeView
from .views import RegisterUserView, RegisterDoneView
from .views import user_activate

app_name = 'main'
urlpatterns = [
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/register/done', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/logout/', ScheduleLogoutView.as_view(), name='logout'),
    path('accounts/password/change/', SchedulePasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/headcheck/', head_check, name='headcheck'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', ScheduleLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]