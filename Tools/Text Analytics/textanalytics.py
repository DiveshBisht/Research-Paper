import urllib.request
import json
import csv
import codecs
import time
 
data = [['ISSUE_ID','SENTIMENT','SCORE']]
count = 0

with codecs.open('cleaned.csv', "r",encoding='UTF-8', errors='ignore') as ft:
  csv_reader = csv.reader(ft, delimiter=',')
  next(csv_reader)

  for row in csv_reader:
   issue_id, comment, newline = row
   print(issue_id)

   try:
    # Configure API access
    apiKey = 'f463231b94854888a573e1258268cd5f'
    sentimentUri = 'https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'

    # Prepare headers
    headers = {}
    headers['Ocp-Apim-Subscription-Key'] = apiKey
    headers['Content-Type'] = 'application/json'
    headers['Accept'] = 'application/json'

    # Determine sentiment
    postData2 = json.dumps({"documents":[{"id":"1", "language":"en", "text":comment}]}).encode('utf-8')
    request2 = urllib.request.Request(sentimentUri, postData2, headers)
    response2 = urllib.request.urlopen(request2)
    response2json = json.loads(response2.read().decode('utf-8'))
    score = response2json['documents'][0]['score'] # Sample json: {'errors': [], 'documents': [{'id': '1', 'score': 0.946106320818458}]}
    
    if(score >= 0.75):
      label='pos'
    elif(score <=0.25):
      label='neg'
    else:
      label='neu' 

   except:
       label = 'invalid'
       score = 'invalid'

   data.append([issue_id, label, score])
   count = count+1

   if(count == 30):
    count=0
    time.sleep(120)


ft.close() 

with open('textanalytics.csv','w',newline='',encoding="utf-8") as fp:
  a = csv.writer(fp, delimiter=',')
  a.writerows(data) #data should be list of lists

fp.close()
