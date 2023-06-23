from django.urls import path
from . import views
from .views import AdvDeleteView

app_name = 'additional_information'
urlpatterns = [
     path('ad_delete/<int:pk>/', views.AdvDeleteView.as_view(), name='ad_delete'),
     path('details_view/<int:pk>/', views.AdvEditView, name='details_view'),
     path('ad_workplace/', views.AdvertisementWorkPlace, name='ad_workplace'),
     path('ad_create/', views.CreateAdvertisement, name='ad_create'),
     path('main/', views.AdvertisementList, name='info_main'),
     path('question_create/', views.QuestionCreate, name='question_create'),
     path('question_list/', views.QuestionList, name='question_list'),
]