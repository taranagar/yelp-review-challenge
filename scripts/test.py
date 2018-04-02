#!/usr/bin/python
import csv
from textblob import TextBlob
# import json

infile = '../data_sample/file.csv'
wordfile = '../dict/food.csv'
temp = []

with open(wordfile, 'r') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:
		word1 = row[0]
		temp.append(word1)

with open(infile, 'r') as csvfile:
	# with open('review_sample.json') as json_data:
	rows = csv.reader(csvfile)
	# d = json.load(json_data)
	for row in rows:
		review = TextBlob(row[0])
		for sentence in review.sentences:
			food = 0
			print sentence
			for word in sentence.words:
				if word in temp:
					food = 1
					if (food == 1):
						print("food was %f ", sentence.sentiment.polarity)
						print ("\n")
						#print(d)
