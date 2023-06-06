from django.contrib import admin
from .models import AdvUser, HeadTeacher, Teacher
from .models import Student, StudyGroup, Course, Classroom, LessonName


# Register your models here.
class AdvUserAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'patronymic', '__str__', 'is_activated', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fields = (('username', 'email', 'phone'), ('first_name', 'last_name', 'patronymic'),
                'avatar', ('send_messages', 'is_active', 'is_activated'),
              ('is_staff', 'is_superuser'),
              'groups', 'user_permissions',
              ('last_login', 'date_joined'))
    readonly_fields = ('last_login', 'date_joined')


class StudyGroupAdmin(admin.ModelAdmin):
    list_display = 'course', 'name_of_group'

class StudentAdmin(admin.ModelAdmin):
    list_display = ('study_group', 'user')


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('initials', 'user')


class HeadTeacherAdmin(admin.ModelAdmin):
    list_display = 'initials', 'user'


admin.site.register(AdvUser, AdvUserAdmin)
admin.site.register(HeadTeacher, HeadTeacherAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(StudyGroup, StudyGroupAdmin)
admin.site.register(Course)
admin.site.register(LessonName)