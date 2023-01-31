from tech_news.database import find_news


# Requisito 10
def top_5_news():
    result = find_news()
    if len(result) < 5:
        return result
 
    # /** 
    # max_count retirada de:
    # Source:
    # https://stackoverflow.com/a/73050/17053855
    # */
    newlist = sorted(result, key=lambda d: d['comments_count'], reverse=True)
    limeted_newlist = newlist[:5]

    list_tuple = []
    for element in limeted_newlist:
        list_tuple.append((element["title"], element["url"]))

    print("\n", list_tuple)

    return list_tuple


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
