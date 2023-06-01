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