#!/usr/bin/python

import json
from pprint import pprint

data = []
ids = []

# open review.json file to read from
with open('../../data/business_ids3.json', 'r') as dataf:
    for line in dataf:
        ids.append(json.loads(line))
ids = ids[0]
dataf.close()

# Number of Business/Business IDs:
print "# Business IDs:", len(ids)


# open review.json file to read from
with open('../../../yelp-data/review.json', 'r') as rf:
    for line in rf:
        line_json = json.loads(line)
        # if review matches with one of our business_ids
        if str(line_json['business_id']) in ids:
            data.append(line_json)
rf.close()

# Number of Reviews:
print "# Reviews:", len(data)

# open reviews.json file to write to
with open('../../data/review/reviews3.json', 'w') as wf:
    json.dump(data, wf)
wf.close()
