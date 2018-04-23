#!/usr/bin/python

import json
from pprint import pprint

data1 = []

# open business.json file to read from
with open('../../../yelp-data/business.json', 'r') as rf:
    for line in rf:
        line_json = json.loads(line)
        # SELECT BUSINESSES THAT FOLLOW FOLLOWING CRITERIA:
        ## good for meal - dinner = True
        ## isopen = True
        ## city = Las Vegas
        ## 10 <= review_count <= 20
        ## categories != Fast Food
        if 'GoodForMeal' in line_json['attributes'] and line_json['city'] == 'LA' and line_json['review_count'] >=15 and line_json['review_count'] <=25 and "Restaurants" in line_json['categories'] and "Fast Food" not in line_json['categories']:
            if line_json['attributes']['GoodForMeal']['dinner'] == True:
                data1.append(json.loads(line))
rf.close()

# of businesses that match above criteria
print "# Businesses:", len(data1)

# write ALL business information into businesses.json
'''
with open('../../data/business/businesses3.json', 'w') as wf1:
    json.dump(data1, wf1)
wf1.close()

# write business_id information to business_id.json to match with reviews
with open('../../data/business_ids3.json', 'w') as wf2:
    data2 = [entry['business_id'] for entry in data1]
    json.dump(data2, wf2)
wf2.close()
'''
