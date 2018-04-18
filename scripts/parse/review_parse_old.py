#!/usr/bin/python

import json
from pprint import pprint

data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []

# open review.json file to read from
with open('../../yelp-data/review.json', 'r') as rf:
    # read in first 100 lines
    for line in rf:
        # Donut Tyme
        if 'PJ-VbAtIOso1dqd2frQqqg' in line:
            data1.append(json.loads(line))
        # Geebee's Bar & Grill
        elif 'Uy3_5nLo3sYkAuSX6mjdmg' in line:
            data2.append(json.loads(line))
        # Kinthai
        elif 'u29lf2yPd-qK5ThAS9FRQQ' in line:
            data3.append(json.loads(line))
        # North Forty Saloon and BBQ
        elif 'KYEZATGRY5aD69ZR6VvyWQ' in line:
            data4.append(json.loads(line))
        # Jack's Pub
        elif 'NoSj3hV8Rlz_gUsOL4_EjQ' in line:
            data5.append(json.loads(line))
        # McDonald's
        elif 'k1PkpDm5d5pYJI1K_3UYpw' in line:
            data6.append(json.loads(line))
rf.close()

print len(data1)
print len(data2)
print len(data3)
print len(data4)
print len(data5)
print len(data6)

# open review_sample.json to write to

# Donut Tyme
with open('../data_sample/review_donuttyme.json', 'w') as wf1:
    json.dump(data1, wf1)
wf1.close()
# Geebee's Bar & Grill
with open('../data_sample/review_geebees.json', 'w') as wf2:
    json.dump(data2, wf2)
wf2.close()
# Kinthai
with open('../data_sample/review_kinthai.json', 'w') as wf3:
    json.dump(data3, wf3)
wf3.close()
# North Forty Saloon and BBQ
with open('../data_sample/review_northforty.json', 'w') as wf4:
    json.dump(data4, wf4)
wf4.close()
# Jack's Pub
with open('../data_sample/review_jackspub.json', 'w') as wf5:
    json.dump(data5, wf5)
wf5.close()
# Nathan's Famous
with open('../data_sample/review_nathans.json', 'w') as wf6:
    json.dump(data6, wf6)
wf6.close()
