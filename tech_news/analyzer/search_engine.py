from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    print(title)
    if title == '':
        return []

    case_sentitive = title.lower()
    query = {"title": {"$regex": case_sentitive}}
    result = search_news(query)
    list_tuple = []
    for element in result:
        list_tuple.append((element["title"], element["url"]))
    print('result: 🔥🔥🔥', list_tuple)
    return list_tuple


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
