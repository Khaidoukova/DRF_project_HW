from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from school.models import Lesson, Course, Subscription
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email='admin', password='admin', is_superuser=True)
        self.token = f'Bearer {AccessToken.for_user(self.user)}'
        self.course = Course.objects.create(title='TestCourse', description='TestCourseDescription')
        self.lesson = Lesson.objects.create(
            course=self.course,
            title='test_lesson',
            description='test_lesson_description',
            video_url='https://youtube.com',
            owner=self.user,

        )
        self.client.force_authenticate(user=self.user)

    def test_create_lesson(self):

        data = {
            "title": "test",
            "description": "test",
            "video_url": "https://youtube.com",
            "owner": self.user.pk
        }

        response = self.client.post(
            reverse('school:lesson_create'),
            data=data,

        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_lesson(self):
        response = self.client.get(
            reverse('school:lesson_list'),
            HTTP_AUTHORIZATION=self.token
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


    def test_update_lesson(self):
        self.client.force_authenticate(self.user)
        data = {
            "title": "test_update_title",
            "video_url": "https://youtube.com",

        }
        response = self.client.patch(
            reverse('school:lesson_update', kwargs={'pk': self.lesson.pk}),
            data=data,
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            Lesson.objects.get(pk=self.lesson.pk).title,
            'test_update_title'
        )


        #self.assertEqual(
        #    response.json(),
        #    {
        #        "id": self.lesson.pk,
        #        "course": self.course.title,
        #        "title": "test_update_title",
        #        "description": self.lesson.description,
        #        "preview": None,
        #        "video_url": "https://youtube.com",
        #        "owner": self.user.pk
        #    }
        #)


    def test_lesson_destroy(self):

        response = self.client.delete(
            reverse('school:lesson_delete', kwargs={'pk': self.lesson.pk}),
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            list(Lesson.objects.all()),
            []
        )

    def tearDown(self):
        self.user.delete()
        self.course.delete()
        self.lesson.delete()


class SubscriptionTestCase(APITestCase):

    def setUp(self):

        self.user = User.objects.create(email='admin', password='admin', is_superuser=True)
        self.token = f'Bearer {AccessToken.for_user(self.user)}'
        self.course = Course.objects.create(title="test", description="test", owner=self.user)

        self.data = {
            'user': self.user,
            'course': self.course
        }

        self.subscription = Subscription.objects.create(**self.data)

    def test_create_subscription(self):

        data = {
            'user': self.user.pk,
            'course': self.course.pk
        }

        response = self.client.post(
            reverse('school:subscription_create'),
            data=data,
            HTTP_AUTHORIZATION=self.token
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
