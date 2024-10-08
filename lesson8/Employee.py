import requests
# import random


class Employee:

    def __init__(self, url):
        self.url = url

    def get_token(self, user='raphael', password='cool-but-crude'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()['userToken']

    def get_employee_list(self, id):
        resp = requests.get(self.url + '/employee?company=' + str(id))
        return resp.json()

    def add_new_employee(self, parameters):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(
            self.url + '/employee', headers=my_headers, json=parameters)
        return resp.json()

    def get_employee_to_id(self, id):
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()

    def edit_employee(self, id_employee, parameters):
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.patch(
            self.url + '/employee/' + str(
                id_employee), headers=my_headers, json=parameters)
        return resp.json()

    # def delete_employee(self, id_employee):
    #     my_headers = {}
    #     my_headers["x-client-token"] = self.get_token()
    #     resp = requests.get(
    #         self.url + '/employee/delete/' + str(id), headers=my_headers)
    #     return resp.json()
