## Ce programme permet de générer un modèle de langue à partir d'un corpus de phrases pour plusieurs langues
##
##
import pandas as pd
import re
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.feature_extraction.text import CountVectorizer
from pickle import dump
import os

if not os.path.exists('models'):
 os.makedirs('models')

data = pd.read_csv("data_traning/LanguageDetection.csv", sep='\t')

X = data["sentence"]
y = data["language"]

##for  col in data.columns:
## print (col)
##exit()
# do something with series

le = LabelEncoder()
y = le.fit_transform(y)


dump(le, open('models/label_model.pkl', 'wb'))

data_list = []
for text in X:
        text = re.sub(r'[!@#$(),"%^*?:;~`0-9]', ' ', text)
        text = re.sub(r'[[]]', ' ', text)
        # converting the text to lower case
        text = text.lower()
        # appending to data_list
        data_list.append(text)


cv = CountVectorizer()

X = cv.fit_transform(data_list).toarray()
dump(cv, open('models/model_cv.pkl', 'wb'))
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)


model = MultinomialNB()
model.fit(x_train, y_train)
dump(model, open('models/language_model.pkl', 'wb'))
y_pred = model.predict(x_test)

ac = accuracy_score(y_test, y_pred)

print ('tiseddi n tneɣruft:', ac)
