#!/usr/bin/python

#open the csv file
import csv

dataToWrite = []

with open('../data_sample/yelp_business.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        cats = row[-1]
#get the restaurants and put in a list
        categories = cats.split(';')
        if (cats == 'categories'):
            dataToWrite.append(row)
        else:
            if 'Restaurants' in cats or 'Food' in cats or 'Bars' in cats:
                dataToWrite.append(row)

#write to restaurants.csv
fileToWrite = open('../data_sample/restaurants.csv', 'w')
with fileToWrite:
    writer = csv.writer(fileToWrite)
    writer.writerows(dataToWrite)