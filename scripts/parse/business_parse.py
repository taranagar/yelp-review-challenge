#!/usr/bin/python

import json
from pprint import pprint

data1 = []

# open review.json file to read from
with open('../../../yelp-data/business.json', 'r') as rf:
    # read in first 100 lines
    for line in rf:
        line_json = json.loads(line)
        if 'GoodForMeal' in line_json['attributes'] and line_json['is_open'] == 1 and line_json['city'] == 'Las Vegas' and line_json['review_count'] >=20 and line_json['review_count'] <=50 and "Restaurants" in line_json['categories'] and "Fast Food" not in line_json['categories']:
            if line_json['attributes']['GoodForMeal']['dinner'] == True:
                data1.append(json.loads(line))
rf.close()

print "# Matching:", len(data1)

with open('../../data/business/businesses.json', 'w') as wf1:
    json.dump(data1, wf1)
wf1.close()

del data1[:]
