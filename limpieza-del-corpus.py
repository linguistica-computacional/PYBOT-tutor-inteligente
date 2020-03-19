#Instalar la libreria nltk, usar el siguiente comando:
#pip install nltk
import nltk
nltk.download("stopwords") #Para instalar el paquete de stopwords
#Para instalar todos los paquetes, utilice en la terminal, el siguiente comando:
#python -m nltk.downloader all

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer
from string import punctuation

stopword = stopwords.words('spanish')
snowball_stemmer = SnowballStemmer('spanish')
wordnet_lemmatizer = WordNetLemmatizer()

def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

dataset = 0
add = input('Enter from Continue add question or 1 from EXIT:  ')
#Se recomienda cambiar por el corpus de tranning

while True:
    if add == '':
        dataset = input('Question:  ')
        #question = processtext.clear(dataset)
        #processtext.writering()
        lowertext = dataset.lower()  # Convertir en minusculas
        signtext = strip_punctuation(lowertext)  # Eliminar puntos de puntuacion
        word_tokens = nltk.word_tokenize(signtext)  # Tokenizar las palabras
        removing_stopwords = [word for word in word_tokens if word not in stopword]  # Eliminar las stopwords (palabras vacías como la, un, los, etc)
        stemmed_word = [snowball_stemmer.stem(word) for word in removing_stopwords]  # Determina la raiz de la palabra y elimina el resto
        lemmatized_word = [wordnet_lemmatizer.lemmatize(word) for word in removing_stopwords]  #
        sent_token = nltk.sent_tokenize(signtext)  # No puede recibir como parametro word_tokens, lemmatized_word and stemmed_word

        f = open('trainning/conversation.yml', 'a') 
        #No se debe manipular los archivos de esta forma, se recomienda cambiar por with open("nuevo_texto.txt", "w") as archivo:
        #    archivo.writelines(["Enhorabuena.\n","Ha creado un archivo de forma segura."])
        f.write('r'+str(stemmed_word)+"'")
        f.write("\n")
        f.close()

        answer = input('Which answer:  ')
        f = open('trainning/conversation.yml', 'a')
        f.write("'"+str(answer)+"'")
        f.write("\n")
        f.close()

        add = input('Enter from Continue add question or 1 from EXIT:  ')

    elif add == '1':
        break

print('End')