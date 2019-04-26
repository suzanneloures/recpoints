import pandas as pd
from surprise import Reader, Dataset, SVD, evaluate
import json


def load_json():
    with open('data/review.json') as json_file:  
        dataset = json.load(json_file)
        return dataset

def train(uid, iid):
    dataset = load_json()   
    df = pd.DataFrame.from_dict(dataset, orient='columns') #json para df
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df[['user_id', 'item_id', 'rating']], reader)
    trainset = data.build_full_trainset()
    svd = SVD()
    svd.fit(trainset)
    pred = svd.predict(uid, iid)
    score = pred.est
    print(score)

train(999,'59392558')