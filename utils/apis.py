import requests

class APIS:
    base_url = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.head = {
            "Content-Type":"application/json"

        }

    def get_call(self,endpoint):
        url = f"{self.base_url}/{endpoint}"
        resp = requests.get(url,headers=self.head)
        return resp

    def post_call(self,endpoint,data):
        url = f"{self.base_url}/{endpoint}"
        resp = requests.post(url,headers=self.head,json=data)
        return resp

    def put_call(self,endpoint,data):
        url = f"{self.base_url}/{endpoint}"
        resp = requests.put(url,headers=self.head,json=data)
        return resp

    def delete_call(self,endpoint):
        url = f"{self.base_url}/{endpoint}"
        resp = requests.delete(url,headers=self.head)
        return resp