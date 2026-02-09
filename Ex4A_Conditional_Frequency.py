import numpy as np
import pandas as pd
import nltk

items = ['apple', 'apple', 'kiwi', 'cabbage', 'cabbage', 'potato']
print(nltk.FreqDist(items))

c_items = [
    ('F','apple'), ('F','apple'), ('F','kiwi'),
    ('V','cabbage'), ('V','cabbage'), ('V','potato')
]

cfd = nltk.ConditionalFreqDist(c_items)
print(cfd.conditions())
cfd.plot()
print(cfd['V'])
