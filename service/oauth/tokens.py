import datetime
from typing import Any

import jose
from jose import jwt

 
def generate_token(username: str, key: str, algorithm: str = "HS256"):
    """ """
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    expire = expire.isoformat()
    data_to_encode = {"username": username, "expire": expire}
    token = jwt.encode(claims=data_to_encode, key=key, algorithm=algorithm)
    return token


def decode_token(token: str, key: str) -> dict[str, Any]:
    data = jwt.decode(token, key)
    # {"username": username, "expire": expire}
    return data
