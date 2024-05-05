import gensim
import numpy as np
import time
import requests
from bs4 import BeautifulSoup
import re
from crawler import Crawler

TIMEOUT = 1000000
class WordAnalyzer:
    def __init__(self):
        self.model = None
        self.build_word2vec_model('glove.6B.100d.txt')

    def build_word2vec_model(self, pretrained_model_path):
        self.model = gensim.models.KeyedVectors.load_word2vec_format(pretrained_model_path, binary=False)

        self.model.fill_norms()

    def find_midpoint(self, word1, word2):
        if word1 not in self.model or word2 not in self.model:
            return None

        vector1 = self.model[word1]
        vector2 = self.model[word2]
        average_vector = (vector1 + vector2) / 2

        closest_word = None
        min_distance = float('inf')

        for word in self.model.index_to_key:
            if word not in [word1, word2]:
                vector = self.model[word]
                distance = np.linalg.norm(average_vector - vector)
                if distance < min_distance:
                    min_distance = distance
                    closest_word = word

        return closest_word



crawler = Crawler()
analyzer = WordAnalyzer()
while(True):
    word1 = input("Enter a word: ")
    word2 = input("Enter another word: ")
    midpoint = analyzer.find_midpoint(word1.lower(), word2.lower())
    print("Midpoint word:", midpoint)
    phrase1 = "https://en.wikipedia.org/wiki/" + word1.capitalize()
    midphrase = "https://en.wikipedia.org/wiki/" + midpoint.capitalize()
    phrase2 = "https://en.wikipedia.org/wiki/" + word2.capitalize()

    path1, logs1, time1, discovered1 = crawler.find_path(phrase1,midphrase)
    print("Path from word1 to midpoint:", path1)
    path2, logs2, time2, discovered2 = crawler.find_path(midphrase,phrase2)
    print("Path from midpoint to word2:", path2)
