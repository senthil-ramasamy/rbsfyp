import csv
import numpy as np
import json
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt

#fb_personlaity_insights
with open('data/fbdata.json') as fb_data_file:    
    fb_data = json.load(fb_data_file)

pprint(fb_data)

#fbdata = open("data/fbdata.json",r)

#twitter_day_wise sentimental_score

twitter_data_na =  pd.read_csv('data/tweets.csv')
twitter_data = twitter_data_na.dropna()
print twitter_data

#logme data

logme_data = pd.read_csv('data/keylog.csv')
print logme_data

#health data march

health_data_na = pd.read_csv('data/sleepdatamarch.csv')
health_data = health_data_na.dropna()
print health_data

#algorithm

#import exisitng dataframes
#normalise and aggregate them to required format excluding nan
#standarise the dataset
#manually tag the three priorites for each column header
#find the covarience and the approximate values to drop and take in the candidate key pair
#find correlation value according to relational header tags
#caluclate the aggregagted relational value based on priorites
#find negative correlation & positive correlation values

#this is not the one we require
#tag each field with three prioritised column fields
#find correlation value

#print health_data.corr()[health_data]
print twitter_data.loc[[3]]


quantified_data = pd.read_csv('data/onlineminsdata.csv')

corr=quantified_data.apply(lambda s: quantified_data.corrwith(s))
print corr

plt.matshow(corr)
plt.xlabel(list(quantified_data))
plt.ylabel(list(quantified_data))
plt.show()



#regression
#pca
#isometric mapping

