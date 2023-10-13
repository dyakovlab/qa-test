from api.base_api import BaseApi


class ReqresApi(BaseApi):

    def get_users(self, params):
        get_users_url = 'https://reqres.in/api/users'
        response = self.get(get_users_url + params)
        result = response.json()
        return result

    def create_user(self, data):
        create_user_url = 'https://reqres.in/api/users'
        response = self.post(create_user_url, data)
        result = response.json()
        return result
