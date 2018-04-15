#!/usr/bin/python

#open the csv file
import csv

dataToWrite = []
restaurant_ids = set()
first = True
first2 = True

#get list of business_id of restaurants
with open('../data_sample/restaurants.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if first:
            first = False
        else:
            restaurant_ids.add(row[0])
print list(restaurant_ids)[:50]
num = 0
            
with open('../data_sample/yelp_review.csv') as csvfile2:
    readCSV2 = csv.reader(csvfile2, delimiter=',')
    for row in readCSV2:
        if first2:
            dataToWrite.append(row)
            first2 = False
        else:
            bus_id = row[2]
            if bus_id in restaurant_ids:
                dataToWrite.append(row)
                num += 1
        if (num == 750000):
            break
                
fileToWrite = open('../data_sample/restaurant_reviews.csv', 'w')
with fileToWrite:
    writer = csv.writer(fileToWrite)
    writer.writerows(dataToWrite)