#!/usr/bin/python

import csv
import json
from textblob import TextBlob

# review file
reviews = json.load(open('../data_sample/review_sample.json'))

# rating categories & their respective dictionary files to be read in as words
# food, ambiance, price, service
categories = ['Food', 'Ambiance', 'Price', 'Service']
files = ['../dict/food.csv', '../dict/ambiance.csv',
'../dict/price.csv', '../dict/service.csv']
words = []

# read dictionary CSV files into words for each rating category
for i, file in enumerate(files):
	# open dictionary file
	with open(file, 'r') as csvfile:
		rows = csv.reader(csvfile)
		# add words in file to words list
		words.append([row[0] for row in rows])

# look through each entry in reviews JSON
for i, entry in enumerate(reviews):
	# review_str - string version of review entry
	# review_tb - textblob version of review entry
	review_str = entry["text"].encode('ascii', 'ignore')
	review_tb = TextBlob(review_str)

	# print entry #, rating, and review
	print "#:", (i+1)
	print "Rating:", entry["stars"]
	print "Review:", review_str[:100],"..."

	# create list of sentiment values for each category
	sents = []

	# loop through each category of words
	for k, w in enumerate(words):
		temp_sent = []
		temp_words = []

		# loop through each sentence in review
		for sentence in review_tb.sentences:
			# do a sentiment analysis of the sentence if it contains word(s) in our target category
			if list(set(sentence.split(" ")) & set(w)):
				temp_words.append(list(set(sentence.split(" ")) & set(w)))
				temp_sent.append(sentence.polarity)
		temp_words = list(set([item for sublist in temp_words for item in sublist]))

		#print out words in review entry that fall under our categories
		if temp_words: print categories[k], "Words:", ', '.join(temp_words)
		else: print categories[k], "Words: N/A"
		sents.append(temp_sent)

	# loop though sentiments of all categories
	for i, sent in enumerate(sents):
		# print out sentiment value of each category
		if sent: print categories[i],"Sentiment:",round(sum(sent)/len(sent),2)
		else: print categories[i],"Sentiment: N/A"
	print
