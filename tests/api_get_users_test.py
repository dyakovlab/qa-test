from api.reqres_api import ReqresApi
from helper.validator import validate_email


class TestApiGetUsers:

    def test_api(self):
        data_keys = ['page', 'per_page', 'total', 'total_pages', 'data', 'support']
        user_keys = ['id', 'email', 'first_name', 'last_name', 'avatar']

        reqres_api = ReqresApi()
        data = reqres_api.get_users('?page=2')

        for data_key in data:
            assert data_key in data_keys, 'Response not contain key'

        for user in data['data']:
            for user_key in user:
                if user_key == 'email':
                    assert validate_email(user['email']), 'User email is not valid. Email: ' + user['email']
                assert user_key in user_keys, 'User not contain key'
