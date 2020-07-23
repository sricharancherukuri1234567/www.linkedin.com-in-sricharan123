from bs4 import BeautifulSoup
import requests
import nltk 
from newspaper import Article
import csv
import json
csv_file = open('file1.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['company url','company name and title','short_description','summary','pricing'])

url1 = 'http://aytm.com'
source = requests.get(url1).text
soup = BeautifulSoup(source,'lxml')
title1 = soup.title
title1 = title1.text

short_desc1 = soup.findAll('p')[8].text


article1 = Article(url1)
article1.download()
article1.parse()
nltk.download('punkt')
article1.nlp()
summary1 = article1.text


url2 = 'http://www.datawallet.com'
source = requests.get(url2).text
soup = BeautifulSoup(source,'html.parser')
title2 = soup.title
title2 = title2.text

short_desc2 = soup.findAll('p')[0].text


article2 = Article(url2)
article2.download()
article2.parse()
nltk.download('punkt')
article2.nlp()
summary2 = article2.text

url3 = 'https://www.fancyhands.com/'
source = requests.get(url3).text
soup = BeautifulSoup(source,'lxml')
title3 = soup.title
title3 = title3.text
pricing = 'yes'
short_desc3 = soup.findAll('h2')[1].text


article3 = Article(url3)
article3.download()
article3.parse()
nltk.download('punkt')
article3.nlp()
summary3 = article3.text


url4 = 'https://starmind.ai/'
source = requests.get(url4).text
soup = BeautifulSoup(source,'lxml')
title4 = soup.title
title4 = title4.text

short_desc4 = soup.findAll('h1')[0].text



article4 = Article(url4)
article4.download()
article4.parse()
nltk.download('punkt')
article4.nlp()
summary4 = article4.text


url5 = 'http://stackoverflow.com'
source = requests.get(url5).text
soup = BeautifulSoup(source,'lxml')
title5 = soup.title
title5 = title5.text

short_desc5 = soup.findAll('p')[5].text


article5 = Article(url5)
article5.download()
article5.parse()
nltk.download('punkt')
article5.nlp()
summary5 = article5.text

tuple1 = [url1,title1,short_desc1,summary1,pricing]
csv_writer.writerow(tuple1)
print(json.dumps(tuple1))


tuple2 = [url2,title2,short_desc2,summary2,pricing]
csv_writer.writerow(tuple2)
print(json.dumps(tuple2))

tuple3 = [url3,title3,short_desc3,summary3,pricing]
csv_writer.writerow(tuple3)
print(json.dumps(tuple3))

tuple4 = [url4,title4,short_desc4,summary4,pricing]
csv_writer.writerow(tuple4)
print(json.dumps(tuple4))


tuple5 = [url5,title5,short_desc5,summary5,pricing]
print(json.dumps(tuple5))
csv_writer.writerow(tuple5)