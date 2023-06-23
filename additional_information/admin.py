from django.contrib import admin
from .models import Questions, Advertisement


# Register your models here.
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('email', 'topic')


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'published')


admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Advertisement, AdvertisementAdmin)
