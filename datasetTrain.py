#import libraries
from curses import window
from tkinter import Frame
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