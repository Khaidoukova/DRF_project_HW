
from django.contrib import admin

from school.models import Lesson, Course, Payment

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'preview', 'description', 'owner',)
    list_filter = ('title',)



@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'video_url', 'course', 'owner',)
    list_filter = ('course', 'owner',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_date', 'payed_course', 'payed_lesson', 'amount', 'payment_method',)