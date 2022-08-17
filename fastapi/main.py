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
        #user history api 받아오기 + 전처리 -> 
        # input =  ["dafasd","adfasdf","Asdfasdf","dfasdgs"]
        return predict(input_) #json
        """
        {
            "rs": ["오삼불고기", "라면", "응애"],
        }
        """

@app.get("/category_rs")
def category_rs():
    with session_factory() as session:
        #input = num(int)
        #user history api 받아오기 + 전처리
        """
        {
            "label_id": "22"
        }
        """
        #pred 함수 call
        return pred #"오삼불고기"
        """
        {
            "group_rs": "오삼불고기"
        }
        """

@app.get("/category_label")
def category_label():
    with session_factory() as session:
        #user history api 받아오기 + 전처리
        #pred 함수 call

        #input = ["dafasd","adfasdf","Asdfasdf","dfasdgs"]
        return pred #1

         """
        {
            "label_id": "22" #0~300
        }
        """