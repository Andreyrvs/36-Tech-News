from tech_news.database import find_news


# Requisito 10
def top_5_news():
    result = find_news()

    # /**
    # max_count retirada de:
    # Source:
    # https://stackoverflow.com/a/73050/17053855
    # */
    sort_title = sorted(result, key=lambda result: result['title'])
    sort_comments = sorted(
        sort_title, key=lambda sort_title: sort_title['comments_count']
    )
    sort_comments.reverse()
    limited_newlist = sort_comments[:5]

    list_tuple = [(item["title"], item["url"]) for item in limited_newlist]

    print("\n", list_tuple)

    return list_tuple


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
