#!/usr/bin/python

import csv
import json
import re
from textblob import TextBlob
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
tb = Blobber(analyzer=NaiveBayesAnalyzer())

# review file
reviews = json.load(open('../data_sample/review_sample.json'))

# rating categories & their respective dictionary files to be read in as words
# food, ambiance, price, service
categories = ['Food', 'Ambiance', 'Price', 'Service']
files = ['../dict/food.csv', '../dict/ambiance.csv',
'../dict/price.csv', '../dict/service.csv']
dictionaries = []

# read dictionary CSV files into words for each rating category
for i, file in enumerate(files):
	# open dictionary file
	with open(file, 'r') as csvfile:
		rows = csv.reader(csvfile)
		# add words in file to words list
		dictionaries.append([row[0] for row in rows])

# conjunction word file used to split sentences into clauses - NOT DONE YET
CC = []
with open('../dict/food.csv', 'r') as csvfile:
		rows = csv.reader(csvfile)
		# add words in file to words list
		CC.append([row[0] for row in rows])

# look through each entry in reviews JSON
for i, entry in enumerate(reviews):
	# review_str - string version of review entry
	# review_tb - textblob version of review entry
	review_str = entry["text"].encode('ascii', 'ignore')
	review_tb = tb(review_str)

	# print entry #, rating, and review
	print "#:", (i+1)
	print "Rating:", entry["stars"]
	print "Review:", review_str[:500],"..."

	# create list of sentiment values for each sentence
	sentiments = [sentence.sentiment.p_pos for sentence in review_tb.sentences]
	print "Individual Sentiments:", sentiments
	print "Overall Sentiment:", review_tb.sentiment

	# create list of keywords in each sentence
	words = [sentence.words.lower().lemmatize() for sentence in review_tb.sentences]
	#print(words)

	# create my list of sentiment values specific to each category
	my_sentiments = []
	# loop through each category
	for j, w in enumerate(dictionaries):
		# add list of all sentiment values for each sentence that contains words in that category
		temp_sent = [sent for k,sent in enumerate(sentiments) if set(words[k]) & set(dictionaries[j])]
		# return average value of sentence sentiments if sentiment values exist
		if temp_sent:
			my_sentiments.append(round(sum(temp_sent)/len(temp_sent),2))
		# if not applicable, return N/A indicating there were no sentences containing words of category, therefore nothing to analyze.
		else:
			my_sentiments.append('N/A')

	# loop though sentiments of all categories
	for l, sent in enumerate(my_sentiments):
		# print out sentiment value of each category
		print categories[l],"Sentiment:",my_sentiments[l]
	print
