import requests


class ToDoList:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_list_of_tasks(self):
        resp = requests.get(self.base_url)
        return resp

    def add_task(self, title):
        my_json = {
            'title': title,
            'completed': False
        }

        resp = requests.post(self.base_url, json=my_json)
        return resp

    def change_title_task(self, task_id: str, title: str):
        my_json = {
            'title': title
        }

        resp = requests.patch(self.base_url + str(task_id), json=my_json)
        return resp

    def delete_task(self, task_id: str):
        resp = requests.delete(self.base_url + str(task_id))
        return resp

    def get_task(self, task_id):
        resp = requests.get(self.base_url + str(task_id))
        return resp

    def task_completed(self, task_id):
        my_json = {
            'completed': True
        }

        resp = requests.patch(self.base_url + str(task_id), json=my_json)
        return resp

    def task_uncompleted(self, task_id):
        my_json = {
            'completed': False
        }

        resp = requests.patch(self.base_url + str(task_id), json=my_json)
        return resp
