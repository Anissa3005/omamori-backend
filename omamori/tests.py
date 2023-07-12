from django.test import TestCase
from django.urls import reverse
from .models import Users, Omamori


class UsersModelTest(TestCase):
    def test_users_model_exists(self):
        users = Users.objects.count()

        self.assertEqual(users, 0)

    def test_model_has_string_representation(self):
        user = Users.objects.create(username="testUser")

        self.assertEqual(str(user), user.username)


class OmamoriModelTest(TestCase):
    def setUp(self):
        # Create a user for testing
        user = Users.objects.create(
            id=1, username="test1", email="test1@example.com")

        self.user_id = Users.objects.get(pk=1)

    def test_omamori_model_exists(self):
        omamori = Omamori.objects.count()

        self.assertEqual(omamori, 0)

    def test_model_has_string_representation(self):
        omamori = Omamori.objects.create(
            users_id=self.user_id, shrine_name="test shrine", location=[35.652832, 139.839478], description="test test test")

        self.assertEqual(str(omamori), omamori.shrine_name)


class UsersRequest(TestCase):
    def setUp(self):
        # Create a user for testing
        Users.objects.create(
            id=1, username="test1", email="test1@example.com")

    def test_create_new_user_return_correct_status_code(self):
        response = self.client.post(
            '/user/', {"username": "test2", "email": "test2@example.com"})
        print(response)

        self.assertEqual(response.status_code, 201)

    def test_get_users_return_correct_status_code(self):
        response = self.client.get('/user/')

        self.assertEqual(response.status_code, 200)

    def test_get_user_by_id_correct_status_code(self):
        url = reverse('user-by-id', kwargs={'id': 1})
        response = self.client.get(path=url)

        self.assertEqual(response.status_code, 200)
