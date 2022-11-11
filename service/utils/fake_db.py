fake_db = {
    "John Doe": {
        "user_name": "John Doe",
        "password": "kcolsnrq",
        "is_admin": True,
    },
    "bbb": {
        "user_name": "bbb",
        "password": "mm38doc6",
        "is_admin": False,
    },
}


def get_user(user_name) -> dict:
    return fake_db.get(user_name, {})
