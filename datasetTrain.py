#import libraries
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import random
import string
import numpy as np
import nltk
import warnings
warnings.filterwarnings("ignore")

#open dataset
f = open('dataset.txt', 'r', errors='ignore')

raw = f.read()
raw = raw.lower() #convert to lowercase

sent_tokens = nltk.sent_tokenize(raw) #convert to list of sentences
word_tokens = nltk.sent_tokenize(raw) #convert to list of words

sent_tokens[:2]
word_tokens[:5]

lemmer = nltk.stem.WordNetLemmatizer() #Text normalization

def LemTokens(tokens):
    return[lemmer.lemmatize(token)for token in tokens]

remove_punct_dict = dict((ord(punct), None)for punct in string.punctuation)

def LemNormalize(text):
    return LemNormalize(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


Introduce_Ans = ["My name is AgroBot.", "My name is AgroBot you can called me Agro.", "Im AgroBot :) ",
                 "My name is AgroBot. and my nickname is Agro and I am happy to solve your queries :) "]
GREETING_INPUTS = ("hello", "hi", "hiii", "hii", "hiiii",
                   "hiiii", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "hii there",
                      "hi there", "hello", "I am glad! You are talking to me"]


#Checking for greetings
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


#Checking for Introduce
def IntroduceMe(sentence):
    return random.choice(Introduce_Ans)
