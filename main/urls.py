from django.urls import path
from .views import index, other_page
from .views import ScheduleLoginView
from .views import profile
from .views import ScheduleLogoutView
from .views import ChangeUserInfoView

app_name = 'main'
urlpatterns = [
    path('accounts/logout/', ScheduleLogoutView.as_view(), name='logout'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', ScheduleLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]