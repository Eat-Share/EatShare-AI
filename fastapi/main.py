from fastapi import FastAPI

import sys
sys.path.append("C:/Users/cpprh/Documents/GitHub/EatShare-AI")
import food_rs
from food_rs import *
from category_rs import *
from pydantic import BaseModel

app = FastAPI()
#initialize()
#model.initialize()
#initialize_()

class food_In(BaseModel):
    historys: list

class food_Out(BaseModel):
    rs: list

class category_rs_In(BaseModel):
    labelId: int

class category_rs_Out(BaseModel):
    group_rs: str

class label_In(BaseModel):
    historys: list

class label_Out(BaseModel):
    label_id: int

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/food_rs",response_model = food_Out)
def food_rs(user_history:food_In):
    
        #user history api 받아오기 + 전처리 -> 
        # input =  ["dafasd","adfasdf","Asdfasdf","dfasdgs"]
     #return predict(user_history) #json
     return predict("오삼불고기")

@app.post("/category_rs",response_model = category_rs_Out)
def category_rs(label_id:category_rs_In):
    #with session_factory() as session:
        #input = num(int)
        #user history api 받아오기 + 전처리
        #pred 함수 call
     return category_rs_(22) #"오삼불고기"


@app.post("/category_label",response_model = label_Out)
def category_label(user_history:label_In):
    #with session_factory() as session:
        #user history api 받아오기 + 전처리
        #pred 함수 call

        #input = ["dafasd","adfasdf","Asdfasdf","dfasdgs"]
    return category_label_("라면")