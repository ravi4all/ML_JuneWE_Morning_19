import pandas as pd
import pickle
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def textProcessing(data):
    tokens = []
    for i in range(len(data)):
        tokens.append(word_tokenize(data['Review'].iloc[i].lower()))
    engStopwords = stopwords.words('english')
    engStopwords.extend(['.','?',"'s","also",",","-","!"])
    
    wordList = []
    for tokenList in tokens:
        t = []
        for token in tokenList:
            if token not in engStopwords:
                t.append(token)
        wordList.append(t)
        
    wnet = WordNetLemmatizer()
    
    for i in range(len(wordList)):
        for j in range(len(wordList[i])):
            wordList[i][j] = wnet.lemmatize(wordList[i][j], pos='v')
    
    for i in range(len(wordList)):
        wordList[i] = ' '.join(wordList[i])
    
    return wordList

def testPrediction(review):
    file = open('model.pkl','rb')
    reg = pickle.load(file)
    file.close()
    file = open("tfidf.pkl",'rb')
    tfidf = pickle.load(file)
    file.close()
    test_df = pd.DataFrame({"Review":[review]})
    wordList = textProcessing(test_df)
    matrix = tfidf.transform(wordList)
    pred = reg.predict(matrix)
    return pred