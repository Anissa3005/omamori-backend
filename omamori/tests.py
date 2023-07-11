from django.test import TestCase
from .models import Users, Omamori


class UsersModelTest(TestCase):
    def test_users_model_exists(self):
        users = Users.objects.count()

        self.assertEqual(users, 0)

    def test_model_has_string_representation(self):
        user = Users.objects.create(username="testUser")

        self.assertEqual(str(user), user.username)


class OmamoriModelTest(TestCase):
    def test_omamori_model_exists(self):
        omamori = Users.objects.count()

        self.assertEqual(omamori, 0)

    # def test_model_has_string_representation(self):
    #     omamori = Omamori.objects.create(
    #         users_id=1, shrine_name="test shrine", location=[35.652832, 139.839478], description="test test test")

    #     self.assertEqual(str(omamori), omamori.shrine_name)


class IndexPageTest(TestCase):
    def test_create_new_user_return_correct_response(self):
        response = self.client.post(
            '/user/', {"username": "test1", "email": "test1@example.com"})

        self.assertEqual(response.status_code, 201)

    def test_get_users_return_correct_response(self):
        response = self.client.get('/user/')

        self.assertEqual(response.status_code, 200)
