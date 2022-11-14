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
- Passing headers by curl 
```
curl -X 'POST' \
  'http://0.0.0.0:8000/v1/?username=joe&password=123' \
  -H 'accept: application/json' \
  -d '' -H 'Authorization:bearer' \
  -H 'client_secret:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImpvZSIsImV4cGlyZSI6IjIwMjItMTEtMTJUMTI6MjM6MzQuMjEyNDg3In0.plFNglaHGnmfOC-bH6pAUhhq9-Cmb3-YBBF2JkPDBYI'
```