import json
import requests
import csv
import codecs
url = 'http://text-processing.com/api/sentiment/'
data = [['ISSUE_ID','SENTIMENT','NEGATIVE','NEUTRAL','POSITIVE']]

with codecs.open('cleaned.csv', "r",encoding='UTF-8', errors='ignore') as ft:
  csv_reader = csv.reader(ft, delimiter=',')
  next(csv_reader)

  for row in csv_reader:
    issue_id, comment, newline = row #unpacking of elements of list into individual variables
    payload = {'text': comment}
    req = requests.post(url, data=payload)
    negative = req.json()['probability']['neg']
    positive = req.json()['probability']['pos']
    neutral = req.json()['probability']['neutral']
    label = req.json()['label']
    data.append([issue_id, label, negative, neutral, positive])
 
ft.close()
with open('nltk.csv','w',newline='') as fp:
   csv_writer = csv.writer(fp, delimiter=',')
   csv_writer.writerows(data)

fp.close()


