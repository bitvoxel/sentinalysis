import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")


def create_sentiment(rating):

    if rating == "negative":
        return -1  # negative sentiment
    elif rating == "positive":
        return 1  # positive sentiment
    else:
        return 0  # neutral sentiment


def clean_data(review):
    no_punc = re.sub(r"[^\w\s]", "", review)
    no_digits = "".join([i for i in no_punc if not i.isdigit()])
    return no_digits


def model(df=pd.read_csv("/workspaces/codespaces-blank/senti/backend/chat.csv")):
    df["sentiment"] = df["sentiment"].apply(create_sentiment)
    df["message"] = df["message"].apply(clean_data)
    vectorizer = CountVectorizer(stop_words=stopwords.words("english"))

    X_train, X_test, y_train, y_test = train_test_split(
        df["message"],
        df["sentiment"],
        test_size=0.25,
        random_state=42
    )
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = LogisticRegression()
    model.fit(X_train_vec, y_train)
    predictions = model.predict(X_test_vec)
    print("Accuracy", accuracy_score(y_test, predictions))

    new_reviews = [input("Enter sentence:")]
    new_reviews_vec = vectorizer.transform(new_reviews)
    predictions = model.predict(new_reviews_vec)
    print(predictions)

model()
