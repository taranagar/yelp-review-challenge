#!/usr/bin/python
import csv
from textblob import TextBlob
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer

tb = Blobber()

sentence = tb("I love this movie, because the actors are so beautiful, talented, and funny.")
sentence2 = tb("I love this restaurant.")

print(sentence)
print(tokenize(sentence))
print(sentence2)
print(sentence2.sentiment)
