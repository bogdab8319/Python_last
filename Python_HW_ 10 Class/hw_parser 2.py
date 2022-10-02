# from typing import List, Dict, Any
#
# import requests
# from bs4 import BeautifulSoup
# import csv
#
# HOST = 'https://www.miraton.ua/ua/'
# URL = 'https://www.miraton.ua/ua/catalog/women/shoes/tufli/'
# HEADERS = {
#     'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)/'
#                   ' Chrome/105.0.0.0 Safari/537.36'
# }
# CSV = 'shoses.csv'
#
#
# def get_html(url, params=" "):
#     r = requests.get(url, headers=HEADERS, params=params)
#     return r
#
#
# def get_content_Women(html):
#     # global shoses
#     # print(shoses)
#     soup = BeautifulSoup(html, 'html.parser')
#     items = soup.find_all('div', class_='section-catalog-items gray-items')
#     if html.status_code == 200:
#         shoses = []
#
#         for item in items:
#             # noinspection PyUnresolvedReferences
#             shoses.append(
#                 {
#                     'product_info': item.find('div', class_='product_info').get_text(strip=True),
#                     'product_brand': item.find('div', class_='product_info').get_text(strip=True),
#                     'product_name': HOST + item.find('div', class_='product_info').find('a').get('href'),
#                     'price': item.find('div', class_='product_price').find / ('price-old',
#                                                                               'price-current').get_text(strip=True),
#                     'product-size-list': item.find('div', class_='product_hover').find('razmer').get('a'),
#
#                 }
#             )
#
#         return shoses
#
#
# def save_doc(item, path, items=None):
#     with open(path, "w", newline=" ") as file:
#         writer = csv.writer(file, delimiter=",")
#         writer.writerow(['Название продуукта: ', 'Бренд: ', 'Описание модели: ', 'Размер: ', 'Цена: '])
#         for item in items:
#             writer.writerow(
#                 [item['product_info'], item['product_brand'], item['product_name'], item['product-size-list'],
#                  item['price'], ])
#
#
# def parser() -> object:
#     PAGENATION = input('Укажите количество страниц для парсинга')
#     PAGENATION = int(PAGENATION.strip())
#     html = get_html(URL)
#     if html.status_code == 200:
#         shoses = []
#         for page in range(1, PAGENATION):
#             print(f'Парсим стр. : {page}')
#             html = get_html(URL, params={'page': page})
#             shoses.extend(get_content_Women(html.text))
#             save_doc(shoses, CSV)
#
#     else:
#         print('Error')
#
#
# parser()





# html = get_html(URL).text()
# print(get_content_Women(html))

# import requests
# from bs4 import BeautifulSoup
# import csv
# 
# HOST = 'https://mir-obuvi.com/'
# URL = 'https://mir-obuvi.com/catalog/2/men/'
# HEADERS = {
#     'accept': ' application/json, text/javascript, */*; q=0.01',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)/'
#                   ' Chrome/105.0.0.0 Safari/537.36'
# }
# 
# 
# def get_html(url, params=" ", ):
#     r = requests.get(url, headers=HEADERS, params=params)
#     return r
# 
# 
# def get_content_men(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     items = soup.find_all('div', id='catalog')
#     shoses: list[dict[str, str]] = []
#     for item in items:
#         shoses.append(
#             {
#                 'brand-name': item.find('span', class_='brand-name').get_text(strip=True),
#                 'goods-name': item.find('span', class_='goods-name').get_text(strip=True),
#                 'price': HOST + item.find('span', class_='price').find('ins').get_text(strip=True),
# 
#                 'sizes': item.find('div', class_='sizes').find('a').get('href', 'rel')
# 
#             }
#         )
# 
#     return shoses
# 
# 
# html = get_html(URL)
# print(get_content_men(html))








import requests
from bs4 import BeautifulSoup


url =' https://mir-obuvi.com/'

# headers= {
#     "Accept":"application/json, text/javascript, */*; q=0.01",
#          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
# }
req= requests.get(url)
src= req.text
# print(src)
with open('index.html',"w") as file:
    file.write(src)
#
# with open('index.html')as file:
#     src= file.read()

soup = BeautifulSoup(src, 'lxml')
all_products_hrefs = soup.find_all(claas_='//bufet.ua/products/sup-ramen/')
for item in all_products_hrefs:
    print(item)
