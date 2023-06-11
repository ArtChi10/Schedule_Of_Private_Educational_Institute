from django.contrib import admin
from .models import Lesson, Classroom
# Register your models here.


class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_name', 'name_of_group', 'classroom', 'teacher', 'date_of_lesson', 'number_of_slot',
                    'info_for_lesson')


class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('number_of_classroom',)


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Classroom, ClassroomAdmin)
