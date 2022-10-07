#import libraries
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

from nltk.stem.porter import PorterStemmer

import random
import string
import numpy as np
import nltk

# nltk.download('wordnet')

# import nltk
# from nltk.stem import WordNetLemmatizer
# nltk.download('popular', quiet=True) # for downloading popular      
# # packages

# # * first-time use only
# nltk.download('punkt') 
# nltk.download('wordnet')

import warnings
warnings.filterwarnings("ignore")

#open dataset
f = open('tea_cultivation_dataset2.txt', 'r', errors='ignore')
m = open('tea_cultivation_dataset1.txt', 'r', errors='ignore')

raw = f.read() #separated sections file
rawone = m.read()

# print('rawone')
# print(rawone)

raw = raw.lower() #convert to lowercase
rawone = rawone.lower() #convert to lowercase

#separated sections file
sent_tokens = nltk.sent_tokenize(raw) #convert to list of sentences
word_tokens = nltk.sent_tokenize(raw) #convert to list of words


sent_tokensone = nltk.sent_tokenize(rawone) #convert to list of sentences
word_tokensone = nltk.sent_tokenize(rawone) #convert to list of words

# print(sent_tokensone)
print(word_tokens)

# sent_tokens[:2]
# sent_tokensone[:2]
# word_tokens[:5]
# word_tokensone[:5]

lemmer = nltk.stem.WordNetLemmatizer() #Text normalization

def LemTokens(tokens):
    return[lemmer.lemmatize(token)for token in tokens]

remove_punct_dict = dict((ord(punct), None)for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


Introduce_Ans = ["My name is AgroBot.", "My name is AgroBot you can called me Agro.", "I'm AgroBot :) ",
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


small_talk_responses = {
'how are you': 'I am fine. Thankyou for asking ',
'how are you doing': 'I am fine. Thankyou for asking ',
'how do you do': 'I am great. Thanks for asking ',
'how are you holding up': 'I am fine. Thankyou for asking ',
'how is it going': 'It is going great. Thankyou for asking ',
'goodmorning': 'Good Morning ',
'goodafternoon': 'Good Afternoon ',
'goodevening': 'Good Evening ',
'good day': 'Good day to you too ',
'whats up': 'The sky ',
'sup': 'The sky ',
'thanks': 'Dont mention it. You are welcome ',
'thankyou': 'Dont mention it. You are welcome ',
'thank you': 'Dont mention it. You are welcome '
}

small_talk = small_talk_responses.values()
small_talk = [str (item) for item in small_talk]

def tfidf_cosim_smalltalk(doc, query):
   query = [query]
   tf = TfidfVectorizer(use_idf=True, sublinear_tf=True)
   tf_doc = tf.fit_transform(doc)
   tf_query = tf.transform(query)
   cosineSimilarities = cosine_similarity(tf_doc,tf_query).flatten()
   related_docs_indices = cosineSimilarities.argsort()[:-2:-1]
   if (cosineSimilarities[related_docs_indices] > 0.7):
      ans = [small_talk[i] for i in related_docs_indices[:1]]
      return ans[0]

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
        
# f = open('Dataset.csv', 'r', encoding='utf-8')
# reader = csv.reader(f)
# corpus = {}
# for row in reader:
#    corpus[row[0]] = {row[1]: row[2]}
   
# all_text = corpus.values()
# all_text = [str (item) for item in all_text]

all_text = word_tokens

# print(all_text)

def stem_tfidf(doc, query):
   query = [query]
   p_stemmer = PorterStemmer()
   
   tf = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')

   
   # tf = TfidfVectorizer(use_idf=True, sublinear_tf=True, stop_words='english')
   
   stemmed_doc = [p_stemmer.stem(w) for w in doc]
   stemmed_query = [p_stemmer.stem(w) for w in query]
   
   tf_doc = tf.fit_transform(stemmed_doc)
   tf_query = tf.transform(stemmed_query)
   
   return tf_doc, tf_query

def cos_sim(a, b): #tf_doc, tf_query
   cosineSimilarities = cosine_similarity(a, b).flatten()
   related_docs_indices = cosineSimilarities.argsort()[:-2:-1]
   
   print(cosineSimilarities[related_docs_indices])
   
   if (cosineSimilarities[related_docs_indices] > 0.1):
      ans = [all_text[i] for i in related_docs_indices[:1]]
      
      ans = ' '.join(ans)
      return ans
      # for item in ans:
      #    c, d = item.split(':')
      #    return d
   else:
      k = 'I am sorry, I cannot help you with this one. Hope to in the future. Cheers :)'
      return k


# #Generating response
# def response(user_response):
#     bot_response = ''
    
#     # find special keywords in user input / user_response then try to generate the bot response accordingly
#     # sent_tokens.append(user_response) #??
    
#     user_response = [user_response]
    
#     TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    
    
#     # tfidf = TfidfVec.fit_transform(sent_tokens)
#     tfidf = TfidfVec.fit_transform(user_response)
#     vals = cosine_similarity(tfidf[-1], tfidf)
#     idx = vals.argsort()[0][-2]
#     flat = vals.flatten()
#     flat.sort()
    
#     req_tfidf = flat[-2]
#     if(req_tfidf == 0):
#         bot_response = bot_response + "I am sorry! I don't understand you"
#         return bot_response
#     else:
#         bot_response = bot_response + sent_tokens[idx]
#         return bot_response

# https://medium.com/analytics-vidhya/a-simple-chatbot-using-python-and-nltk-c413b40e9441

#Generating response lemos
def response(user_response):
    bot_response = ''
    
    # find special keywords in user input / user_response then try to generate the bot response accordingly
    # sent_tokens.append(user_response) #??
    
    # user_response = [user_response]
    
    # TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    
    
    a, b = stem_tfidf(all_text, user_response)
    g = cos_sim(a, b)
    # print('\nNate: '+g)
    print('Nate')
    print(g)
    
    return g
    
    # req_tfidf = flat[-2]
    # if(req_tfidf == 0):
    #     bot_response = bot_response + "I am sorry! I don't understand you"
    #     return bot_response
    # else:
    #     bot_response = bot_response + sent_tokens[idx]
    #     return bot_response


#Generating response
def responseone(user_response):
    bot_response = ''
    sent_tokensone.append(user_response)
    
    
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    
    tfidf = TfidfVec.fit_transform(sent_tokensone)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf == 0):
        bot_response = bot_response + "I am sorry! I don't understand you"
        return bot_response
    else:
        bot_response = bot_response + sent_tokensone[idx]
        return bot_response


def Agro(user_response):
    user_response = user_response.lower()
    # keyword = " module "
    # keywordone = " module"
    # keywordsecond = "module "

    if (user_response != 'bye'):
        if (user_response == 'thanks' or user_response == 'thank you'):
            return "You are welcome.."
        else:
            # if (user_response.find(keyword) != -1 or user_response.find(keywordone) != -1 or user_response.find(keywordsecond) != -1 != None):
            # if (user_response.find(keyword) != -1 or user_response.find(keywordone) != -1 or user_response.find(keywordsecond) != -1):
            #     return responseone(user_response)
            if (greeting(user_response) != None):
                return greeting(user_response)
            elif (user_response.find("your name") != -1 or user_response.find(" your name") != -1 or user_response.find("your name ") != -1 or user_response.find(" your name ") != -1):
                return IntroduceMe(user_response)
            elif(tfidf_cosim_smalltalk(small_talk_responses, user_response)!=None):
                return tfidf_cosim_smalltalk(small_talk_responses, user_response)
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
