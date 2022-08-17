import pandas as pd
import json
import textrank
from konlpy.tag import Komoran

def initialize():
    komoran = Komoran()
    df = pd.read_csv('./category_label.csv', index_col=0)
    df = pd.DataFrame(df)

def komoran_tokenizer(sent):
    words = komoran.pos(sent, join=True)
    words = [w for w in words if ('/NN' in w)]
    return words

def category_label(str_):
    return df[df["NN"] == komoran_tokenizer(str_)[-1][:-4]].iloc[0, 2] #ex) 22

def category_rs(num):
    return df[df["category"] == num].iloc[2, 0] #ex) '¿À»ïºÒ°í±â'