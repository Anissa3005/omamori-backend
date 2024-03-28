from django.test import TestCase, Client


class UserAuthenticationTestCase(TestCase):
    def setUp(self) -> None:
        client = Client()
        new_user = {"username": "fred", "password": "secret"}
        client.post('/users/signin/', new_user)

    def test_user_can_create_account(self) -> None:
        client = Client()
        new_user = {"username": "frogman", "password": "secret"}

        response = client.post('/users/signin/', new_user)

        self.assertEqual(response.status_code, 201)
        self.assertGreater(response.data['id'], 0)

    def test_user_can_login(self) -> None:
        client = Client()
        user = {"username": "fred", "password": "secret"}

        response = client.post('/users/login/', user)

        self.assertEqual(response.status_code, 202)
        self.assertTrue(response.data)
        self.assertTrue(client.cookies)

    def test_user_can_logout(self) -> None:
        client = Client()
        # We first want to login to beable to set our jwt token in cookie
        user = {"username": "fred", "password": "secret"}
        client.post('/users/login/', user)

        response = client.post('/users/logout/')

        self.assertEqual(response.status_code, 202)
        self.assertEqual(response.data, {'message': 'Logout succesful'})
        self.assertEqual(client.cookies['jwt'].value, '')
