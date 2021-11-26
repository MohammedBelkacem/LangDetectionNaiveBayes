## Ce programme permet de classer des phrases d'un corpus qui contient des phrases mélangées de 15 langues différentes
##
##

from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from pickle import load
import os

if not os.path.exists('test_classification'):
 os.makedirs('test_classification')

le = LabelEncoder()
le = load(open('models/label_model.pkl', 'rb'))

cv = CountVectorizer()
cv = load(open('models/model_cv.pkl', 'rb'))

model = MultinomialNB()
model = load(open('models/language_model.pkl', 'rb'))


#16

tutlayin=['kab','eng','fra','ita','eus','cat','por','spa','deu','nld','swe','est','srp','tur','hun','rus']
tifyar=[]
for i in tutlayin:
    tifyar.append([])
a=[]
def asismel (afaylu, model,cv,le):
    afaylu_arawway=open(afaylu,encoding='utf-8')
    for sentence in afaylu_arawway:
        sentence=sentence.replace('\n','')
        x = cv.transform([sentence]).toarray() # converting text to bag of words model (Vector)
        lang = model.predict(x) # predicting the language
        lang = le.inverse_transform(lang) # finding the language corresponding the the predicted value
        if lang in tutlayin:
            a=tifyar[tutlayin.index(lang)]
            a.append(sentence)
            tifyar[tutlayin.index(lang)]=a

afaylu="data_test/Brut.csv"
asismel (afaylu,model,cv,le)

for i in tutlayin:

       afaylu_yemmden= open("test_classification/"+i+".txt","w+",encoding='utf-8')
       for j in tifyar[tutlayin.index(i)]:
        afaylu_yemmden.write(j+"\n")
       afaylu_yemmden.close()


print("finished")
