from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    if title == '':
        return []

    case_sentitive = title.lower()
    query = {"title": {"$regex": case_sentitive}}
    result = search_news(query)
    list_tuple = []
    for element in result:
        list_tuple.append((element["title"], element["url"]))
    return list_tuple


# Requisito 7
def search_by_date(date):

    try:
        date_format = '%Y-%m-%d'
        date_object = datetime.datetime.strptime(date, date_format)
        print('date_object: ', date_object)
    except ValueError:
        raise ValueError("Data inválida")

    inverted_date = datetime.datetime.strptime(date, '%Y-%m-%d').strftime("%d/%m/%Y")
    query = {"timestamp": {"$regex": inverted_date}}
    result = search_news(query)
    list_tuple = []

    for element in result:
        if inverted_date not in element["timestamp"]:
            return []
        list_tuple.append((element["title"], element["url"]))

    return list_tuple


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
