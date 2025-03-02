# 🍃 AgroBot – Tea Disease Diagnosis Chatbot

![AgroBot](/images/readme_image.png)

AgroBot is an AI-powered chatbot designed to assist tea farmers in diagnosing plant diseases and providing treatment suggestions. It leverages Natural Language Processing (NLP) and Machine Learning to analyze user queries and provide expert agricultural advice.

## 📌 Features

- [x] AI Chatbot for Tea Disease Diagnosis – Detects common tea plant diseases.
- [x] NLP-based Query Processing – Understands farmer queries in natural language.
- [x] Disease Identification & Remedies – Provides solutions for detected diseases.

## 🛠️ Technologies Used
- Programming Language: Python (NLP)
- Natural Language Processing (NLP): NLTK, scipy, numpy, etc.
- Machine Learning: Scikit-Learn


## 🚀 Installation Guide
```sh
## Clone the repository
git clone https://github.com/nuwanthaDilshan/AgroBot.git

## Navigate to the project directory
cd AgroBot

```
```sh
##  Install required dependencies
pip install -r requirements.txt

```

```sh

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True) # for downloading popular      
packages

```

```sh
* first-time use only
nltk.download('punkt') 
nltk.download('wordnet')
```
```sh
## Run the chatbot application
python app.py

```

## 🤝 Contributing
##### We welcome contributions!

1. Fork the repository
2. Create a feature branch (feature/new-functionality)
3. Commit your changes (git commit -m "Added new feature")
4. Push to the branch (git push origin feature/new-functionality)
5. Create a Pull Request

