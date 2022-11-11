import datetime

import jose
from jose import jwt


def generate_token(user_name, key, algorithm="HS256"):
    """ """
    expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    expire = expire.isoformat()
    data_to_encode = {"user_name": user_name, "expire": expire}
    token = jwt.encode(claims=data_to_encode, key=key, algorithm=algorithm)
    return token


def decode_token(token, key):
    return jwt.decode(token, key)
