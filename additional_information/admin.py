from django.contrib import admin
from .models import Questions


# Register your models here.
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('email', 'topic')


admin.site.register(Questions, QuestionsAdmin)