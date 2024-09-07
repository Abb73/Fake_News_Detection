import pickle
import pandas as pd
import string
with open('GBCModel.pkl', 'rb') as f:
    GBC = pickle.load(f)
with open('vectorizer.pkl', 'rb') as f:
     vectorization= pickle.load(f)
# ttext formating
import re
def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text
#from sklearn.feature_extraction.text import TfidfVectorizer



# output formatting
def output_lable(n):
    if n == 0:
        return "Fake News"
    elif n == 1:
        return "Not A Fake News"
class predict:
    def manual_testing(self,news):
        testing_news = {"text":[news]}
        new_def_test = pd.DataFrame(testing_news)
        new_def_test["text"] = new_def_test["text"].apply(wordopt)
        new_x_test = new_def_test["text"]
        new_xv_test = vectorization.transform(new_x_test)


        pred_GBC = GBC.predict(new_xv_test)
        return  output_lable(pred_GBC[0])
   
    

