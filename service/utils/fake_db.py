fake_db = {
    "John Doe": {
        "username": "John Doe",
        "password": "kcolsnrq",
        "is_admin": True,
    },
    "joe": {
        "username": "joe",
        "password": "123",
        "is_admin": False,
    },
}


def get_user(username) -> dict:
    return fake_db.get(username, {})
