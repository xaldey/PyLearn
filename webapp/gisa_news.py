import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False

# def get_python_news():
#     html = get_html("https://www.python.org/blogs/")
#     if html:
#         soup = BeautifulSoup(html, 'html.parser')
#         all_news = soup.find('ul', class_='list-recent-posts').findAll('li')
#         result_news = []
#         for news in all_news:
#             title = news.find('a').text
#             url = news.find('a')['href']
#             published = news.find('time').text
#             result_news.append({
#                 "title": title,
#                 "url": url,
#                 "published": published
#             })
#         return result_news
#     return False

def get_gisa_news():
    html = get_html("http://gisa.ru/")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        soup.findAll('A')
        #print(soup)
        # for news in all_gisa_news:
        #     title = news.find('a').text
        #     url = news.find('A')['href']
        #     published = news.find('time').text
        #     result_gisa_news.append({
        #         "title": title,
        #         "url": url,
        #         "published": published
        #     })
        #     print(result_gisa_news)
        # return result_gisa_news

    return False

