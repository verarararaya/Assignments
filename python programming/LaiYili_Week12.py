# Week 12 - Assessed exercises

# This week we learnt some advanced data manipulation methods, about APIs and
# about webscraping. In this last set of assessed exercises you must complete the
# Brightspace quiz 'W12 - Assessed exercises' and submit a .py file with the 
# code you used to answer the questions in your quiz. Each question is work
# 0.5 marks and it is either correct (full marks) or incorrect (0 marks).

# This template file contains code that will help you answer the questions in 
# the quiz.

# Q1 and Q2 are based on the advanced data manipulation section. You will need to 
# use the titantic dataset which is part of the seaborn package and can be loaded
# using the following commands
import seaborn as sb
titanic = sb.load_dataset('titanic')
# The questions involve using the groupby function and applying functions to that
# grouped object. For questins involving the interquartile range, use the function
# from lecture_12_code.py
def IQR(x):
    return x.quantile(0.75)-x.quantile(0.25)
titanic_gr = titanic.groupby(['sex','survived']).fare
print(round(titanic_gr.mean()))
titanic_gr2 = titanic.groupby(['sex','pclass','survived'])
print(titanic_gr2.count())
print(round(titanic_gr2.agg(IQR)))
# Q3 to Q5 relate to the World Bank API. You will be asked to search of indicator
# and country codes in Q3 and Q4. In Q5 you will need to extract data from the 
# the World Bank for a particular indicator, country and year
import wbdata as wbd
import datetime
print(wbd.search_countries('Bolivia'))
print(wbd.search_indicators('Taxes on income, profits and capital gains'))
country = ['IN']
indicator = {'GC.TAX.YPKG.RV.ZS': 'Taxes on income, profits and capital gains (% of current revenue)'}
data_date = (datetime.datetime(2001, 1, 1), datetime.datetime(2001,12,31))
data = wbd.get_dataframe(indicator,country,data_date)
print(round(data))

# print(wbd.get_dataframe())
# Q6 to Q8 relate to webscraping and uses the Spotify weekly charts. You will need
# to import BeautifulSoup and the requests package
from bs4 import BeautifulSoup
import requests
import numpy as np
# The below code loads the data from the Spotify weekly charts for the week
# 2017-06-30 to 2017-07-07, and uses BeautifulSoup to parse the html.
spotify = requests.get('https://spotifycharts.com/regional/global/weekly/2017-06-30--2017-07-07')
soup = BeautifulSoup(spotify.text, "html.parser")

# The following commands extract the information related to the tracks and removes
# the html tags
track = soup.find_all('td',class_="chart-table-track")
tracks = [x.text.strip() for x in track]
# Q6 asks you to search through tracks to find the number of times a particular
# arist appears in this weekly chart
sum = 0
for tra in tracks:
    sum = sum + tra.count('Kygo')
print(sum)
# The following commands extract the information related to the number of plays,
# removes the html tags and commas, and converts the value to an integers
play = soup.find_all('td',class_="chart-table-streams")
plays = [int(x.text.strip().replace(',', '')) for x in play]
# Q7 asks you to perform some statistical analysis on these numbers
print(round(np.std(plays,ddof=1)))
# Q8 asks you to load the charts for a different week and determine how many of
# the songs from the original week 2017-06-30 to 2017-07-07 are still in the 
# charts at this later week. To load in the data for the new week, change the
# date range in the url to the date range specified in your question. 
spotify1 = requests.get('https://spotifycharts.com/regional/global/weekly/2018-06-29--2018-07-06')
soup1 = BeautifulSoup(spotify1.text, "html.parser")
song = soup1.find_all('td',class_="chart-table-track")
songs = [x.text.strip() for x in song]
print(len(list(set(tracks)&set(songs))))
