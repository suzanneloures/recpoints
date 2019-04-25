import pandas as pd
from surprise import Reader, Dataset, SVD, evaluate

review = ({'user_id': ['0', '0', '0', '1', '1', '2', '2', '2'],
                     'item_id': ['a', 'b', 'c', 'a', 'b', 'b', 'c', 'd'],
                     'rating': [1, 3, 2, 5, 4, 1, 4, 3]})
df = pd.DataFrame(review)
#rating_scale param is requiered.
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['user_id', 'item_id', 'rating']], reader)
print (df)
# treina com toda  a base
trainset = data.build_full_trainset()

# define o algoritmo 
algo = SVD()

result = evaluate(algo, data, measures=['RMSE'])

uid = str(0)  
iid = str('b') 

# get a prediction for specific users and items.
pred = algo.predict(uid, iid, r_ui=1, verbose=True)