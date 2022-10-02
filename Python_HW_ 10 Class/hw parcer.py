
# import time
# from threading import Thread
# import requests
# from lxml import html

# def price_nasdaq(emt):
#     url = f'https://finance.yahoo.com/quote/{emt}'
#     xPath: str = '//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[1]/text()'
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         tree = html.fromstring(response.text)
#         price = tree.xpath(xPath)
#         print(f'{emt}: {price[0]}')
#
#
# names = ['NIO', 'GOOG', 'TSLA', 'KWEB', 'MOHO', 'AAPL', 'META', 'MSFT']
# start = time.perf_counter()
# # for name in names:
# #     price_nasdaq(name)
# # end = time.perf_counter()
# # print(f'time wthout threads = {end - start:0.2f}')
#
# start:float = time.perf_counter()
# threads = []
# for name in names:
#     t = Thread(target=price_nasdaq, args=(name,))
#     t.start()
#     threads.append(t)
#
# for t in threads:
#     t.join()
#
# end = time.perf_counter()
# print(f'time with threads = {end - start:0.2f}')


#
# def name_product(Kh):
#     url = f'https://mir-obuvi.com/ {Kh}'
#
#     response = requests.get(url)
#     tree = html.fromstring(response.text)
#
#     if response.status_code == 200:
#         tree = html.fromstring(response.text)
#         price = tree.xpath(xPath)
#
# start:float = time.perf_counter()
# xPath: str = 'https://mir-obuvi.com/catalog/2/men/text() '
# products = []
#
#
# for product in range(1,len(-1):
#     s = xPath.replace('product(1)'f'product[{i}]')
#     product.append(s)



names = []
for name in names :
    name_product(name)

end = time.perf_counter()
print(f'time wthout threads = {end - start:0.2f}')

start:float = time.perf_counter()
threads = []
for price in products:
    t = Thread(target=name_product, args=(name,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.perf_counter()
print(f'time with threads = {end - start:0.2f}')



def save_function(article_list):
    pass


# def hackernews_rss():
#     article_list = []
#     try:
#         print('Starting the scraping tool')
#         # выполняем запрос, разбираем данные с помощью XML
#         # разбираем данные в BS4
#         r = requests.get('https://news.ycombinator.com/rss')
#         soup = BeautifulSoup(r.content, features='xml')
#         # выбираем из данных только "items", которые нам нужны
#         articles = soup.findAll('item')
#
#         # для каждого "item" разбираем его в список
#         for a in articles:
#             title = a.find('title').text
#             link = a.find('link').text
#             published_wrong = a.find('pubDate').text
#             published = datetime.strptime(published_wrong, '%a, %d %b %Y %H:%M:%S %z')
#             # выводим(published, published_wrong) # проверяем корректность формата даты
#             # создаем объект "article" с данными
#             # из каждого "item"
#             article = {
#                 'title': title,
#                 'link': link,
#                 'published': published,
#                 'source': 'HackerNews RSS'
#             }
#             # добавляем "article_list" с каждым объектом "article"
#             article_list.append(article)
#             print('Finished scraping the articles')
#
#             # после цикла передаем сохраненный объект в файл .txt
#             # return save_function(article_list)
#     except Exception as e:
#         print('The scraping job failed. See exception:')
#         print(e)






import requests
from parse import parse_page
from threading import Thread
from lxml import html


def price_nasdaq(emt):
    url = f'https://favoriteshoes.com.ua/zhinoche-vzuttia/{emt}'
    xPath: str = '//*[@id="content-block"]/main/div[4]/div/div[2]/div[1]/div[2]/div[1]/div/span/text()'
    response = requests.get(url)

    if response.status_code == 200:
        tree = html.fromstring(response.text)
        price = tree.xpath(xPath)
        print(f'{emt}: {price[0]}')



def  get_info(shose):
    info_dict = {}
    name = shose.find('product_title').get_text()
    colection=shose.find('badge new').get_text()
    price = shose.find(' price').get_text()
    info_dict.update({'Название моделі': name, 'Колекція': colection, 'Ціна: ': price })
    print(info_dict)
    return info_dict

# def get_all_shose():
#     threads=[]
#     soup = parse_page(url)
#     shoses = soup.find_all('//*[@id="content-block"]/main/div[4]/div/div[2]')
#     for shose in shoses:
#         t = Thread(target=get_info, args=(shose,))
#         t.start()
#         threads.append(t)
#     for t in threads:
#         t.join()
#
# # get_all_shose()
# print(t)
# #
# #
