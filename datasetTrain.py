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
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


Introduce_Ans = ["My name is AgroBot.", "My name is AgroBot you can called me Agro.", "Im AgroBot :) ",
                 "My name is AgroBot. and my nickname is Agro and I am happy to solve your queries :) "]
GREETING_INPUTS = ("hello", "hi", "hiii", "hii", "hiiii",
                   "hiiii", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "hii there",
                      "hi there", "hello", "I am glad! You are talking to me"]
Basic_Q_1 = ("please help", "help me","please help me","can you help me")
Basic_Ans_1 = ["yes I can", "Tell me", "sure"]
Basic_Q_2 = ("Okay", "okay","ok")
Basic_Ans_2 = ["Is there anything else to know?"]
Basic_Q_3 = ("no", "No","not yet", "Not yet","Nop","nop")
Basic_Ans_3 = ["Okay Thank you Bye", "Have a nice day", "Bye"]
Basic_Q_4 = ("Yes","yes","yeah","Yeah","Yep","Yep")
Basic_Ans_4 = ["What","What else", "Tell me"]



#Checking for greetings
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


#Checking for Introduce
def IntroduceMe(sentence):
    return random.choice(Introduce_Ans)


# Checking for Basic_Q_1
def basic1(sentence):
    for word in Basic_Q_1:
        if sentence.lower() == word:
            return random.choice(Basic_Ans_1)

# Checking for Basic_Q_2
def basic2(sentence):
    for word in Basic_Q_2:
        if sentence.lower() == word:
            return random.choice(Basic_Ans_2)


# Checking for Basic_Q_3
def basic3(sentence):
    for word in Basic_Q_3:
        if sentence.lower() == word:
            return random.choice(Basic_Ans_3)


# Checking for Basic_Q_34
def basic4(sentence):
    for word in Basic_Q_4:
        if sentence.lower() == word:
            return random.choice(Basic_Ans_4)


#Generating response
def response(user_response):
    bot_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf == 0):
        bot_response = bot_response + "I am sorry! I don't understand you"
        return bot_response
    else:
        bot_response = bot_response + sent_tokens[idx]
        return bot_response


def Agro(user_response):
    user_response = user_response.lower()
    keyword = " module "
    keywordone = " module"
    keywordsecond = "module "

    if (user_response != 'bye'):
        if (user_response == 'thanks' or user_response == 'thank you'):
            return "You are welcome.."
        else:
            if (greeting(user_response) != None):
                return greeting(user_response)
            elif (user_response.find("your name") != -1 or user_response.find(" your name") != -1 or user_response.find("your name ") != -1 or user_response.find(" your name ") != -1):
                return IntroduceMe(user_response)
            elif (basic1(user_response) != None):
                return basic1(user_response)
            elif (basic2(user_response) != None):
                return basic2(user_response)
            elif (basic3(user_response) != None):
                return basic3(user_response)
            elif (basic4(user_response) != None):
                return basic4(user_response)
            else:
                return response(user_response)

    else:
        return "Bye! take care.."
