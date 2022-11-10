from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn


load_dotenv()


fake_db = {
	"aaa": {
		"user_name": "aaa", 
		"password": "kcolsnrq", 
		"is_admin": True,
	},
	"bbb": {
		"user_name": "bbb", 
		"password": "mm38doc6", 
		"is_admin": False,
	},
}

app = FastAPI()


@app.post("/token/get")
def getting_token(user_name: str, password: str):
    """     """
    ...
    return {"token": "dummy"}


@app.post("/token/check")
def checking_token(token: str):
    """ """
    ...
    return {"data": "to be implemented"}



if __name__ == "__main__":
    uvicorn.run("service.__main__:app", host="0.0.0.0", port=8000, reload=True)
