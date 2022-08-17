### RUN
```py
uvicorn main:app --reload
```

[http://127.0.0.1:8000](http://127.0.0.1:8000)

#### python 기준으로 input과 return임. input는 json으로 던져주면 이쪽에서 파싱해서 써도됩니당.
### /food_rs
```py
input =  ["dafasd","adfasdf","Asdfasdf","dfasdgs"]
return = {
            "rs": ["오삼불고기", "라면", "응애"],
         }
```

### /category_rs
```py
input = int a
return = {
            "group_rs": "오삼불고기"
         }
```

### /category_label
```py
input =  ["dafasd","adfasdf","Asdfasdf","dfasdgs"]
return = {
            "label_id": "22" #0~300
         }
```
