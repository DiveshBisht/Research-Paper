import json
import urllib.request
import csv

username = input('Enter github username : ')
repo = input('Enter github repository : ')
last_sha=''
data = [['Author','Email','Date','Message',]]

while True:
  default_url = 'https://api.github.com/repos/'+ username + '/' + repo + '/commits?per_page=100&sha=' + last_sha

  with urllib.request.urlopen(default_url) as url:
      response = url.readall().decode('utf-8')
  js = json.loads(response)


  count = 1
  for items in js:
      count = count + 1     
      sha = items["sha"]
      if count==100:
        break
      author = items["commit"]["author"]["name"]
      email = items["commit"]["author"]["email"]
      date = items["commit"]["author"]["date"]
      message = items["commit"]["message"]
      data.append([author,email,date,message])

  if sha==last_sha:
      break
  last_sha = sha    

with open('zookeeper.csv','w',newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(data) #data should be list of lists