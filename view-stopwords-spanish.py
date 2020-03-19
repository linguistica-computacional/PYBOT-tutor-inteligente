#El siguiente codigo es para ver las palabras stopwords que se estan utilizando
#Las stopwords son palabras que no aportan significado a la comprension del texto.

import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words("spanish"))
print(stop_words)