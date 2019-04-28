import pandas as pd
from surprise import Reader, Dataset, SVD, evaluate
import json


def load_json():
    with open('data/review.json') as json_file:  
        dataset = json.load(json_file)
        return dataset

svd = SVD()

def train():
    global svd
    dataset = load_json()   
    df = pd.DataFrame.from_dict(dataset, orient='columns') #json para df
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df[['user_id', 'item_id', 'rating']], reader)
    trainset = data.build_full_trainset()
    svd.fit(trainset)


def predict(uid, iid):
    global svd
    pred = svd.predict(uid, iid)
    score = pred.est
    return score

if __name__ == '__main__':
    train()
    predict(999,'59392558')