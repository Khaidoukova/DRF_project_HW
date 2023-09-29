from rest_framework import serializers

from school.models import Course, Lesson, Payment


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.IntegerField(source='lesson_set.count', read_only=True)
    lessons = LessonSerializer(source='lesson_set', many=True)

    class Meta:
        model = Course
        fields = '__all__'








class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

