#!/usr/bin/python

#import packages
import csv
import json
import re
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
	print "Individual Sentiments:", sentiments
	return sentiments

# create list of words in each sentence
def review_words(review_str):
	words = [sentence.words.lower().lemmatize() for sentence in tb(review_str).sentences]
	#print words
	return words

def categories_sentiments(dictionaries, sentiments, words):
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

##########

##### SENTIMENT ANALYSIS #####

# sentiment analysis for all reviews
def reviews_sentiments(reviews, dictionaries):
	# look through each entry in reviews JSON
	for i, entry in enumerate(reviews[:5]):
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
	reviews = load_review_file('../data_sample/review_sample.json')
	dictionaries = category_files_to_dictionaries(['../dict/food.csv', '../dict/ambiance.csv', '../dict/price.csv', '../dict/service.csv'])
	reviews_sentiments(reviews, dictionaries)
	#review_sentiments("Love the staff, love the meat, love the place. Prepare for a long line around lunch or dinner hours.")

if __name__== "__main__":
	main()
