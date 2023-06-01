from django import forms
from .models import AdvUser
from phonenumber_field.modelfields import PhoneNumberField


class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True, label='Адрес электронной почты')

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'phone', 'first_name', 'last_name', "patronymic", "avatar", 'send_messages')
