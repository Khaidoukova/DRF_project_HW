from rest_framework import serializers

from school.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'




