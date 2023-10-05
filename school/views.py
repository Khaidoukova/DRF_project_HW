from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from school.models import Course, Lesson, Payment
from school.permissions import IsStaff, IsOwner
from school.serializers import CourseSerializer, LessonSerializer, PaymentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsStaff | IsOwner]

    def get_queryset(self):

        if self.request.user.role == self.request.user.is_staff:
            return Course.objects.all()
        else:
            return Course.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):

        if self.request.user == self.request.user.is_staff:
            raise PermissionDenied("Вы не можете создавать новые курсы!")
        else:
            new_course = serializer.save()
            new_course.owner = self.request.user
            new_course.save()

    def perform_destroy(self, instance):

        if self.request.user.role == self.request.user.is_staff:
            raise PermissionDenied("Вы не можете удалять курсы!")
        instance.delete()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):

        if self.request.user == self.request.user.is_staff:
            raise PermissionDenied("Вы не можете создавать новые уроки!")
        else:
            new_lesson = serializer.save()
            new_lesson.owner = self.request.user
            new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsOwner]

    def get_queryset(self):

        if self.request.user == self.request.user.is_staff:
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(owner=self.request.user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsOwner]

    def get_queryset(self):

        if self.request.user == self.request.user.is_staff:
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(owner=self.request.user)


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    ordering_fields = ['date_payment']
    search_fields = ['course__name', 'lesson__name', 'payment_type']
    permission_classes = [IsAuthenticated]


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('payed_course', 'payed_lesson', 'user', 'payment_method', )
    ordering_fields = ('payment_date',)
    permission_classes = [IsAuthenticated]



