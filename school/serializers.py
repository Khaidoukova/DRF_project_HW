from rest_framework import serializers

from school.models import Course, Lesson, Payment, Subscription
from school.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [
            UrlValidator(field='video_url'),
            serializers.UniqueTogetherValidator(fields=['title', 'video_url'], queryset=Lesson.objects.all())
        ]


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.IntegerField(source='lesson_set.count', read_only=True)
    lessons = LessonSerializer(source='lesson_set', many=True)
    is_subscribed = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'

    def get_is_subscribed(self, instance):
        request = self.context.get('request')
        subscription = Subscription.objects.filter(course=instance.pk, user=request.user).exists()
        if subscription:
            return True
        return False


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'
