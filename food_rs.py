import torch
from torch import nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader

from tqdm import tqdm
from tqdm.notebook import tqdm as tqdm_notebook

import pandas as pd
import gluonnlp as nlp
import numpy as np
import json
import random

from transformers.optimization import get_cosine_schedule_with_warmup
from transformers import BertModel
from transformers import AdamW

from kobert.pytorch_kobert import get_pytorch_kobert_model

from kobert_hf.kobert_tokenizer import KoBERTTokenizer


class BERTDataset(Dataset):
    def __init__(self, dataset, sent_idx, label_idx, bert_tokenizer,vocab, max_len,
                 pad, pair):
        transform = nlp.data.BERTSentenceTransform(bert_tokenizer, max_seq_length=max_len,vocab=vocab, pad=pad, pair=pair)
        
        self.sentences = [transform([i[sent_idx]]) for i in dataset]
        self.labels = [np.int32(i[label_idx]) for i in dataset]

    def __getitem__(self, i):
        return (self.sentences[i] + (self.labels[i], ))
         

    def __len__(self):
        return (len(self.labels))


class BERTClassifier(nn.Module):
    def __init__(self,
                 bert,
                 hidden_size = 768,
                 num_classes=7,
                 dr_rate=None,
                 params=None):
        super(BERTClassifier, self).__init__()
        self.bert = bert
        self.dr_rate = dr_rate
                 
        self.classifier = nn.Linear(hidden_size , num_classes)
        if dr_rate:
            self.dropout = nn.Dropout(p=dr_rate)
    
    def gen_attention_mask(self, token_ids, valid_length):
        attention_mask = torch.zeros_like(token_ids)
        for i, v in enumerate(valid_length):
            attention_mask[i][:v] = 1
        return attention_mask.float()

    def forward(self, token_ids, valid_length, segment_ids):
        attention_mask = self.gen_attention_mask(token_ids, valid_length)
        
        _, pooler = self.bert(input_ids = token_ids, token_type_ids = segment_ids.long(), attention_mask = attention_mask.float().to(token_ids.device),return_dict=False)
        if self.dr_rate:
            out = self.dropout(pooler)
        return self.classifier(out)


def initialize():
    global model
	df = pd.read_csv('./dataset_lite.csv', index_col=0)
	df = pd.DataFrame(df)
	final = pd.read_csv('./final.csv', index_col=0)
	final = pd.DataFrame(final)
	bertmodel, vocab = get_pytorch_kobert_model('C:\\Users\\cpprh/.cache\\huggingface\\transformers', '.cache')
	tokenizer = KoBERTTokenizer.from_pretrained('skt/kobert-base-v1')
	tok=tokenizer.tokenize
    device = torch.device("cuda:0")

    max_len = 64
    batch_size = 4
    warmup_ratio = 0.1
    num_epochs = 5  
    max_grad_norm = 1
    log_interval = 200
    learning_rate =  5e-5

    ## 학습 모델 로드
    PATH = './model/'
    model = torch.load(PATH + 'KoBERT_test.pt')  # 전체 모델을 통째로 불러옴, 클래스 선언 필수
    model.load_state_dict(torch.load(PATH + 'model_state_dict.pt'))  # state_dict를 불러 온 후, 모델에 저장
    model.eval()


def predict(predict_sentence):

    data = [predict_sentence, '0']
    dataset_another = [data]

    another_test = BERTDataset(dataset_another, 0, 1, tok, vocab, max_len, True, False)
    test_dataloader = torch.utils.data.DataLoader(another_test, batch_size=batch_size)

    for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(test_dataloader):
        token_ids = token_ids.long().to(device)
        segment_ids = segment_ids.long().to(device)

        valid_length= valid_length
        label = label.long().to(device)

        out = model(token_ids, valid_length, segment_ids)


        test_eval=[]
        for i in out:
            logits=i
            logits = logits.detach().cpu().numpy()

            test_eval.append(np.argmax(logits))

        max_label = np.argmax(test_eval)
        return rs(max_label)


def rs(num):
    rand = random.randrange(1,1000)
    rs_list = []
    for i in range(3):
        rs_list.append(final[final['label'] == num].iat[rand+i,0])
    print(rs)
    json_ = {'rs':rs_list}
    return json.dumps(json_, ensure_ascii=False)