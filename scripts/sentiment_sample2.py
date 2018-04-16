#!/usr/bin/python

#import packages
import csv
import json
import re
import numpy as np
from textblob import TextBlob
from textblob import Blobber
from textblob.sentiments import NaiveBayesAnalyzer
tb = Blobber()

# global variables
reviews = []
dictionaries = []
categories = ['Food', 'Ambiance', 'Price', 'Service']

##### LOADING IN FILES #####

# load json review file in
def load_review_file(review_file):
	reviews = json.load(open(review_file))
	return reviews

# read dictionary CSV files into words for each rating category
def category_files_to_dictionaries(category_files):
	for i, file in enumerate(category_files):
		# open dictionary file
		with open(file, 'r') as csvfile:
			rows = csv.reader(csvfile)
			# add words in file to words list
			dictionaries.append([row[0] for row in rows])
	return dictionaries

##########

##### SENTIMENT ANALYSIS HELPER FUNCTIONS #####

# create list of sentiment values for each sentence
def review_sentiments(review_str):
	#print review_str[:100]
	# review's overall sentiment value
	print "Overall Sentiment:", tb(review_str).polarity
	# review's sentiment values broken down by sentences
	sentiments = [sentence.sentiment.polarity for sentence in tb(review_str).sentences]
	print "Individual Sentence Sentiments:", sentiments
	return sentiments

# create list of words in each sentence
def review_words(review_str):
	words = [sentence.words.lower().lemmatize() for sentence in tb(review_str).sentences]
	#print words
	return words

def categories_sentiments(dictionaries, sentiments, words):
	# create my list of sentiment values specific to each category
	my_sentiments_ave = []
	my_sentiments_std = []
	# loop through each category
	for j, w in enumerate(dictionaries):
		# add list of all sentiment values for each sentence that contains words in that category
		temp_sent = [sent for k,sent in enumerate(sentiments) if set(words[k]) & set(dictionaries[j])]

		# remove very neutral values (-0.05, 0.05)
		temp_sent = filter(lambda a: abs(a > 0.05), temp_sent)
		print "Filtered",categories[j],"Sentiment Values", temp_sent

		# return average value of sentence sentiments if sentiment values exist
		if temp_sent:
			# my_sentiments_ave.append(round(sum(temp_sent)/len(temp_sent),2))
			my_sentiments_ave.append(np.mean(np.array(temp_sent), dtype=np.float64))
			my_sentiments_std.append(np.std(np.array(temp_sent), dtype=np.float64))

		# if not applicable, return N/A indicating there were no sentences containing words of category, therefore nothing to analyze.
		else:
			my_sentiments_ave.append('N/A')
			my_sentiments_std.append('N/A')

	# loop though sentiments of all categories
	for j, sent in enumerate(my_sentiments_ave):
		# print out sentiment value of each category
		print categories[j],"Sentiment (Value Mean):",my_sentiments_ave[j]
		print categories[j],"Sentiment (Value Std):",my_sentiments_std[j]
		print "Sentiment (Stars):", sentiment_value_to_star(my_sentiments_ave[j], my_sentiments_std[j])
	print

# converts sentiment values from (-1, 1) scale to 5-star scale
def sentiment_value_to_star(value_mean, value_std):
	# no mean
	if value_mean == 'N/A':
		return "N/A"
	# TO DO: DETERMINE STANDARD DEVIATION CUTOFF
	# standard deviation too large, we can't determine a star
	elif value_std > 0.5:
		return "Can't Be Determined"
	elif value_mean > 0.6:
		return "5"
	elif value_mean > 0.2:
		return "4"
	elif value_mean > -0.2:
		return "3"
	elif value_mean > -0.6:
		return "2"
	else:
		return "1"
##########

##### SENTIMENT ANALYSIS #####

# sentiment analysis for all reviews
def reviews_sentiments(reviews, dictionaries):
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
		sentiments = review_sentiments(review_str)

		# create list of words in each sentence
		words = review_words(review_str)

		categories_sentiments(dictionaries, sentiments, words)

##########

##### MAIN FUNCTION #####

def main():
	reviews = load_review_file('../data_sample/review_donuttyme.json')
	dictionaries = category_files_to_dictionaries(['../dict/food.csv', '../dict/ambiance.csv', '../dict/price.csv', '../dict/service.csv'])
	reviews_sentiments(reviews, dictionaries)
	#review_sentiments("Love the staff, love the meat, love the place. Prepare for a long line around lunch or dinner hours.")

if __name__== "__main__":
	main()
