#!D:/Python3.X/python.exe
# encoding=utf-8


import json
from collections import defaultdict

def get_counts2(sequence):
    counts=defaultdict(int)
    for x in sequence:
        counts[x]+=1
    return counts

def top_counts(count_dict,n=10):
    value_key_pairs=[(count,tz) for tz,count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]


path='D:/Data/GitHub-Clone/My-Path-Of-Python-Learning/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records=[json.loads(line) for line in open(path)]

time_zones=[rec['tz'] for rec in records if 'tz' in rec]
counts=get_counts2(time_zones)
top_counts(counts)


#Another method:

from collections import Counter

counts=Counter(time_zones)
counts.most_common(10)



#Now, let's use the Pandas module to give an easyer way!

from pandas import DataFrame, Series

import pandas as pd
import numpy as np

frame = DataFrame(records)
