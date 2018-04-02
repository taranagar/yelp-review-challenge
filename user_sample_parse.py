#!/usr/bin/python

import json
from pprint import pprint

data = []
# open review.json file to read from
with open('../yelp-data/user.json') as rf:
    # read in first 100 lines
    for i in range(100):
        line = rf.next().strip()
        data.append(json.loads(line))
rf.close()

# open review_sample.json to write to
with open('data_sample/user_sample.json', 'w') as wf:
    # save 100 review lines into sample json
    json.dump(data, wf)
wf.close()
