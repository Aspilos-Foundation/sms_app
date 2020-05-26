import requests
from bs4 import BeautifulSoup

URL = 'https://ncdc.gov.ng/news/press'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find('tbody')
news_elems = results.find_all('row')
#print(results.prettify())
for news_elem in news_elems:
    title_elem = news_elem.find('h3')
    date_elem = news_elem.find('h4')
    sub_elem = news_elem.find(id='text')
    link_elem = news_elem.find('a', class_='white-text')
    print(title_elem.text.strip())
    print(date_elem.text.strip())
    print(sub_elem.text.strip())
    print(link_elem.text.strip())