"""
Módulo de procesamiento de texto con IA
"""
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

class ProcesadorTexto:
    def __init__(self, idioma='spanish'):
        self.stopwords = set(stopwords.words(idioma))
        self.lematizador = WordNetLemmatizer()

    def limpiar_texto(self, texto):
        texto = texto.lower()
        texto = re.sub(r'[^a-záéíóúñ\s]', '', texto)
        return texto.strip()

    def procesar(self, texto):
        texto_limpio = self.limpiar_texto(texto)
        palabras = word_tokenize(texto_limpio)
        palabras_filtradas = [p for p in palabras if p not in self.stopwords and len(p) > 2]
        return palabras_filtradas