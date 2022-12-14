import datetime

from jose import jwt


def get_data_for_token(username: str) -> dict[str, str]:
    """make dict {"username": username, "expire": expire}"""
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    expire = expire.isoformat()
    data_to_encode = {"username": username, "expire": expire}
    return data_to_encode


def generate_token(username: str, key: str, algorithm: str = "HS256") -> str:
    """make token from username,  key, expiration in timedelta(minutes=30)"""
    data_to_encode = get_data_for_token(username)
    token = jwt.encode(claims=data_to_encode, key=key, algorithm=algorithm)
    return token


def decode_token(token: str, key: str, algorithm: str = "HS256") -> dict[str, str]:
    """data: # {"username": username, "expire": expire}"""
    data = jwt.decode(token, key, algorithms=algorithm)
    return data
