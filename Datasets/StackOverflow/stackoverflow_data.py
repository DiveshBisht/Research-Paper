import json
import urllib.request
import csv
import gzip


data = [['User_ID','User_name','Reputation','Comment','Comment_ID','Date','Post_ID']]
page = 1
count = 0
has_more = True

while (has_more == True) and (count<1000):
    default_url = 'https://api.stackexchange.com/2.2/comments?page='+str(page)+'&pagesize=50&fromdate=1483228800&todate=1504137600&order=desc&sort=creation&site=stackoverflow&filter=withbody'
    with urllib.request.urlopen(default_url) as url:
       response = gzip.decompress(url.read())
       response = str(response, 'utf-8')
    js = json.loads(response)


    for item in js["items"]:
       count = count + 1     
       User_ID = item["owner"]["user_id"]
       User_name = item["owner"]["display_name"]
       Reputation = item["owner"]["reputation"]
       Comment = item["body"]
       Comment_ID = item["comment_id"]
       Date = item["creation_date"]
       Post_ID = item["post_id"]
       data.append([User_ID,User_name,Reputation,Comment,Comment_ID,Date,Post_ID])
   
    has_more = js["has_more"]
    page = page + 1
  
with open('stackoverflow.csv','w',newline='',encoding="utf-8") as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(data) #data should be list of lists

    