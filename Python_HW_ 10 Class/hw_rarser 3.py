import requests
from bs4 import BeautifulSoup
from lxml import html
import json
import csv

url = ' https://bufet.ua/menyu/'

headers = {
    'accept': ' text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
req = requests.get(url)
src = req.text
# print(src)
# with open('index.html',"w") as file:
#     file.write(src)

#
with open('index.html') as file:
    src = file.read()
#
soup = BeautifulSoup(src, 'lxml')
all_products_hrefs = soup.find_all(class_="span3")
all_categories_dict = {}
for item in all_products_hrefs:
    item_text = item.text
    item_href = url + item.get("span3")
    # print(f'{item_text}:: {item_href}')

    all_categories_dict[item_text] = item_href

with open('all_categories_dict.json', "w") as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

with open('all_categories_dict.json') as file:
    all_categories = json.load(file)

for category_name, category_href in all_categories.items():
    req = requests.get(url, category_href, headers=headers)
    src = req.text

    with open(f"{category_name}.html", "w") as file:
        file.write(src)

    with open(f'{category_name}.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    table_head = soup.find(class_='span3').find('div').find_all('li')
    # print(table_head)
    text = table_head[0].text
    price = table_head[1].text
    price_weight = table_head[2].text
    with open(f'{category_name}.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow((text, price, price_weight))



