from fastapi import FastAPI
import model
import sys
sys.path.append("C:/Users/cpprh/Documents/GitHub/EatShare-AI")
import food_rs

app = FastAPI()

model.initialize()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/food_rs")
def food_rs():
    with session_factory() as session:
        #user history api 받아오기 + 전처리 -> input_
        return predict(input_)
    
@app.get("/category_rs")
def category_rs():
    with session_factory() as session:
        #user history api 받아오기 + 전처리
        #pred 함수 call
        return pred

@app.get("/category_rs/{userid}")
def category_rs():
    with session_factory() as session:
        #user history api 받아오기 + 전처리
        #pred 함수 call
        return pred