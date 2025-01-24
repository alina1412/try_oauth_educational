import datetime

import pytz
from jose import jwt

from service.oauth.schemas import TokenDataDto


def get_data_for_token(username: str) -> dict[str, str]:
    """Make dict {"username": username, "expire": expire}"""
    expire = datetime.datetime.now(tz=pytz.utc) + datetime.timedelta(
        minutes=30
    )
    expire = expire.isoformat()
    data_to_encode = {"username": username, "expire": expire}
    return data_to_encode


def generate_token(username: str, key: str, algorithm: str = "HS256") -> str:
    """Make token from username,  key, expiration in timedelta(minutes=30)"""
    data_to_encode = get_data_for_token(username)
    token = jwt.encode(claims=data_to_encode, key=key, algorithm=algorithm)
    return token


def decode_token(
    token: str, key: str, algorithm: str = "HS256"
) -> TokenDataDto:
    data = jwt.decode(token, key, algorithms=algorithm)
    return TokenDataDto(**data)
