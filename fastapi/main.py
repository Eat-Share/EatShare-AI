from fastapi import FastAPI
import model

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/food_rs")
def food_rs():
    with session_factory() as session:
        #user history api 받아오기 + 전처리
        #pred 함수 call
        return pred
    
@app.get("/category_rs")
def category_rs():
    with session_factory() as session:
        #user history api 받아오기 + 전처리
        #pred 함수 call
        return pred