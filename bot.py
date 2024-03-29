from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy
import string
import random
import nltk

f = open('data.txt', 'r', errors='ignore')
row = f.read()

row = row.lower()
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
sentance_tokens = nltk.sent_tokenize(row)
word_tokenize = nltk.word_tokenize(row)
lemmer = nltk.stem.WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punc_dict = dict((ord(punct), None)for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punc_dict)))


greet_inputs = ('hello', 'Hello', 'whatsup', 'how are you?', 'How are you?')
greed_responses = ('hi', 'hay', 'Hey There')


def greet(sentance):
    for word in sentance.split():
        if word.lower() in greet_inputs:
            return random.choice(greed_responses)


def response(user_responce):
    robo1_responce = ''
    Tfidfvc = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = Tfidfvc.fit_transform(sentance_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if (req_tfidf == 0):
        robo1_responce = robo1_responce+"i am sorry.i can not understand"
        return robo1_responce
    else:
        robo1_responce = robo1_responce+sentance_tokens[idx]
        return robo1_responce


flag = True
print("hello ! i am chartbot. start conversion using hello .for ending typing type bye !")
while (flag == True):
    # bind To The Html Page
    user_responce = input("Enter Your Input :-")
    user_responce = user_responce.lower()
    if (user_responce != 'bye'):
        if (user_responce == 'thank you' or user_responce == 'thanks'):
            flag = False
            print('Welcome................')
        else:
            if (greet(user_responce) != None):
                print('Bot '+greet(user_responce))
            else:
                sentance_tokens.append(user_responce)
                word_tokenize = word_tokenize+nltk.word_tokenize(user_responce)
                final = list(set(word_tokenize))
                print('Bot:', end='')
                print(response(user_responce))
                sentance_tokens.remove(user_responce)
    else:
        flag = False
        print('Bot:goodbuy')
