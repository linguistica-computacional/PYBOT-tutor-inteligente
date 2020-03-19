 #El siguiente codigo es

import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
ps = PorterStemmer()
#Detener una lista de palabras

example_words = ["Pythonear","Python","Pythonista"]

for w in example_words:
    print(ps.stem(w))

'''Resultado:
Python
Python
Python'''