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
    # /** linhas 26 a 30 (try/exept) foram retiradas desse site */
    # /** Source:
    # https://www.tutorialspoint.com/How-to-do-date-validation-in-Python
    # */
    try:
        date_format = '%Y-%m-%d'
        date_object = datetime.datetime.strptime(date, date_format)
        print('date_object: ', date_object)
    except ValueError:
        raise ValueError("Data inválida")

    dt = datetime.datetime.strptime(date, '%Y-%m-%d')
    inverted_date = dt.strftime("%d/%m/%Y")
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
    query = {"tags": {"$regex": tag, "$options": "i"}}
    result = search_news(query)
    list_tuple = []
    for element in result:
        list_tuple.append((element["title"], element["url"]))
    return list_tuple


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}
    result = search_news(query)
    list_tuple = []
    for element in result:
        list_tuple.append((element["title"], element["url"]))
    return list_tuple
