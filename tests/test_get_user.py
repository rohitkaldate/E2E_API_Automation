import pytest
from requests import request

from utils.apis import APIS

## This is used to create the object of the class API and it is used in the further test methods/cases.
@pytest.fixture(scope='module')
def apis():
    return APIS()

##Test Case for the GET request
def test_get_user_info(apis):
    response = apis.get_call('users')
    print(response.status_code)
    assert response.status_code == 200
    print(response.json())

## Test Case for the POST request
def test_create_user(apis):
    user_data = {
        "user":"Rohit",
        "username":"rkaldate",
        "email":"kaldaterohit234@gmail.com"
    }
    response = apis.post_call('users',user_data)
    print(response.status_code)
    assert response.status_code == 201
    print(response.json())
    assert response.json()['user'] == "Rohit"
    id = response.json()['id']
    get_id =  apis.get_call('users/10')
    print(get_id.json())

## Test Case for the PUT request
def test_update_user(apis):
    user_data = {
        "user":"rohit k",
        "username":"rkaldate",
        "email":"kaldaterohit234@gmail.com"
    }
    response = apis.put_call('users/10',user_data)
    print(response.status_code)
    assert response.status_code == 200
    print(response.json())
    assert response.json()['user'] == "rohit k"

## Test case to delete the user
def test_delete_user_info(apis):
    response = apis.delete_call('users/1')
    print(response.status_code)
    assert response.status_code == 200
    print(response.json())
