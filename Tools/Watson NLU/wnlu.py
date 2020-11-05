import json
import csv
import codecs
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as Features
data = [['ISSUE_ID','SENTIMENT','SCORE']]

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username="c7adf4ff-bcb3-4331-8046-2871af477334",
  password="2F2p7cS3jjv6",
  version="2017-02-27")

with codecs.open('cleaned.csv', "r",encoding='UTF-8', errors='ignore') as ft:
  csv_reader = csv.reader(ft, delimiter=',')
  next(csv_reader)

  for row in csv_reader:
    issue_id, comment, newline = row
    print(issue_id)

    try:
      response = natural_language_understanding.analyze(
      text=comment,
      features=[Features.Sentiment()]
      ) 
      score = response['sentiment']['document']['label']
      label = response['sentiment']['document']['score']
    except:
      label = 'invalid'
      score = 'invalid'  
    data.append([issue_id, label, score])

ft.close() 

with open('stanfordNLP.csv','w',newline='',encoding="utf-8") as fp:
  a = csv.writer(fp, delimiter=',')
  a.writerows(data) #data should be list of lists

fp.close()
