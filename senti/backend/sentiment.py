# import pandas as pd
# from sklearn.feature_extraction.text import re, TfidfVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score
# import numpy as np

# df = pd.read_csv('/workspaces/codespaces-blank/senti/backend/chat.csv')
# def create_sentiment(rating):
    
#     if rating=='negative':
#         return -1 # negative sentiment
#     elif rating=='positive':
#         return 1 # positive sentiment
#     else:
#         return 0 # neutral sentiment
    


# def clean_data(review):
#     no_punc = re.sub(r'[^\w\s]', '', review)
#     no_digits = ''.join([i for i in no_punc if not i.isdigit()])
#     return(no_digits)

# def processData(string):
#     Dataframe=pd.DataFrame([['message'],[string]])
#     TFI_VECTOR = tfidf.fit_transform(df['message'])
#     return TFI_VECTOR


# df['sentiment'] = df['sentiment'].apply(create_sentiment)
# df['message']=df['message'].apply(clean_data)
# tfidf = TfidfVectorizer(strip_accents=None, 
#                         lowercase=False,
#                         preprocessor=None)
# TFI_VECTOR = tfidf.fit_transform(df['message'])
# TARGET = df['sentiment']
# X_train, X_test, y_train, y_test = train_test_split(TFI_VECTOR,TARGET)
# LogReg = LogisticRegression(solver='sag')
# LogReg.fit(X_train,y_train) # fit the model


# preds = LogReg.predict(X_test) # make predictions
# print(preds.tolist())
# print(y_test)

# Use a pipeline as a high-level helper
# Use a pipeline as a high-level helper
from transformers import pipeline
def classify(text):
    pipe = pipeline("text-classification", model="j-hartmann/sentiment-roberta-large-english-3-classes")
    return pipe(text)
