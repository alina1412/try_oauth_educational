import json


def test_open_handler(client):
    url = "/v1/open/"
    lst = [("joe", 200), ("", 200)]
    for username, code in lst:
        response = client.get(url + f"?{username}=joe")
        assert response.status_code == code


def test_private_handler_unauth(client):
    url = "/v1/"
    username = "joe"
    password = "123"
    token = ""
    answer = b'{"detail":"Incorrect token"}'
    code = 401
   
    response = client.post(
        url + f"?username={username}&password={password}",
        headers={"Authorization": "bearer", "client_secret": token},
    )
    assert response.content == answer
    assert response.status_code == code


def get_test_token(client):
    username = "joe"
    password = "123"
    url = "/auth/v1/token/get"
    response = client.post(url + f"?username={username}&password={password}")
    assert response.status_code == 200
    data = json.loads(response.content)
    # print(data, type(data))
    token = data["token"]
    return token


def test_private_handler_auth(client):
    token = get_test_token(client)
    url = "/v1/"
    response = client.post(
        url + f"?username=joe&password=123",
        headers={"Authorization": "bearer", "client_secret": token},
    )
    assert response.status_code == 200
    data = json.loads(response.content)
    assert "data" in data
    assert "username" in data["data"]
    assert data["data"]["username"] == "joe"
