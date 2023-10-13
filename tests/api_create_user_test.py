from api.reqres_api import ReqresApi


class TestApiCreateUser:

    def test_api(self):
        user_data = {
            'email': 'janet.weaver@reqres.in',
            'first_name': 'Janet',
            'last_name': 'Weaver',
            'avatar': 'https://reqres.in/img/faces/2-image.jpg'
        }

        reqres_api = ReqresApi()
        data = reqres_api.create_user(user_data)
        for key in data:
            if key in user_data:
                assert user_data[key] == data[key], 'User key value is nou equal. Key: ' + key
