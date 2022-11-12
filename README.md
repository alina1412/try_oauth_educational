#### Educational FastApi project for checking usage of jwt tokens and encode(), decode() methods from jose library.

### Tools used:
- poetry
- Makefile
- pytest

### Topics to study:
- Dependencies `from fastapi import Depends`
- Creating tokens `token = jwt.encode(claims=data_to_encode, key=key)`
- Passsing tokens through headers `token = request.headers.get("client_secret")`
- Passing headers in pytest ```response = client.post(url + f"?username={username}&password={password}", 
        headers={"Authorization": "bearer", "client_secret": token})```
- Usage of password hashing ```from passlib.context import CryptContext ...
hasher = CryptContext(schemes=["sha256_crypt", "md5_crypt", "des_crypt"])
...hasher.verify("my-password", hashed_password_from_db)```
