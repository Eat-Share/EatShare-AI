### RUN
```py
uvicorn main:app --reload
```

[http://127.0.0.1:8000](http://127.0.0.1:8000)

#### python �������� input�� return��. input�� json���� �����ָ� ���ʿ��� �Ľ��ؼ� �ᵵ�˴ϴ�.
### /food_rs
```py
input =  ["dafasd","adfasdf","Asdfasdf","dfasdgs"]
return = {
            "rs": ["����Ұ��", "���", "����"],
         }
```

### /category_rs
```py
input =  ["dafasd","adfasdf","Asdfasdf","dfasdgs"]
return = {
            "group_rs": "����Ұ��"
         }
```

### /category_label
```py
input =  ["dafasd","adfasdf","Asdfasdf","dfasdgs"]
return = {
            "label_id": "22" #0~300
         }
```