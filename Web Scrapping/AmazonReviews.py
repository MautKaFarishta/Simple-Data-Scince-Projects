from bs4 import BeautifulSoup as bs
import requests

link='https://www.amazon.in/Test-Exclusive-748/dp/B07DJLVJ5M/ref=sr_1_1?dchild=1&keywords=one+plus+nord&qid=1600016267&sr=8-1'

page=requests.get(link)

soup=bs(page.content,'html.parser')

# print(soup.prettify())

names=soup.find_all('div',{'data-hook':'review'})

print(names)