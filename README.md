#### Educational FastApi project 
for checking usage of jwt tokens and encode(), decode() methods from jose library.

The project has "fake" database, passwords are used just for checking the technology.

### Tools used:
- poetry
- Makefile
- pytest

### Stack:
- FastAPI
- swagger

### Swagger
- "Authorize" button allows to check auth in headers
<img src="https://github.com/user-attachments/assets/cbb4a840-2ec3-4999-b97c-94a03152d992" width="50%">
<img src="https://github.com/user-attachments/assets/bbd9bcd0-db5b-4692-8ca6-f77fa4bc25b4" width="50%">



### Topics to study:
- Dependencies `from fastapi import Depends`
- Creating tokens `token = jwt.encode(claims=data_to_encode, key=key)`
- Passsing tokens through headers `token = request.headers.get("client_secret")`
- Passing headers in pytest ```response = client.post(url + f"?username={username}&password={password}", 
        headers={"Authorization": "bearer xxx", "client_secret": token})```
- Usage of password hashing ```from passlib.context import CryptContext ...
hasher = CryptContext(schemes=["sha256_crypt", "md5_crypt", "des_crypt"])
...hasher.verify("my-password", hashed_password_from_db)```
- Passing headers by curl 
```

example of a request 

curl -X 'POST' \
  'http://0.0.0.0:8000/v1/?username=joe&password=123' \
  -H 'accept: application/json' \
  -d '' -H 'Authorization:bearer xxx' \
  -H 'client_secret:eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImpvZSIsImV4cGlyZSI6IjIwMjUtMDEtMjRUMTQ6Mjg6MDMuMDM2NzI0KzAwOjAwIn0.GTphQVoUy6eBX14hx2UPXv6-4u4tbrgUEWLEHXGLFho'
```
