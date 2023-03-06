import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

on = 1000
data = {'id': [], 'title': [], 'rel': []}


def toInt(x):
  return int(x.replace(',', '').replace(' ', '').replace('min', ''))


while on<8001:
 url = f'https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=num_votes,desc&start={on}'
 print(f'Page: {url}')
 time.sleep(2)
 html_content = requests.get(url,  timeout=60)
 if html_content.status_code != 200:
     print('code broke:'+str(html_content.status_code))
      
 soup = BeautifulSoup(html_content.content, "html.parser")
 cards = soup.find_all('div',class_='lister-item mode-advanced')

 for card in cards:
  eid = float(card.find('h3',class_='lister-item-header').find('span').text.replace(',',''))
  title = card.find('h3',class_='lister-item-header').find('a').text
  x = card.find('div', class_='lister-item-content').find('span',class_='runtime')

  if x:
      rel = toInt(x.text)
  else:
    rel = 0

  data['id'].append(eid)
  data['title'].append(title)
  data['rel'].append(rel)
 on+=50


df = pd.DataFrame(data)
df_sorted = df.sort_values('rel', ascending=False)
print(df)
print('----')
print(df_sorted)

df.to_csv('output.csv', index=False)
df_sorted.to_csv('output_sorted.csv', index=False)

print(f"Max rel:  {df_sorted.loc['row1','col2']}")


