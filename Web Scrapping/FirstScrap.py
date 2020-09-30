from bs4 import BeautifulSoup
import requests

with open('simple.htm') as html_file:
   soup=BeautifulSoup(html_file,'lxml')

print(soup.prettify())

for article in soup.find_all('div',class_='article'):
   head=article.h2.a.text
   print(head)

   summary=article.p.text
   print(summary)

   print()