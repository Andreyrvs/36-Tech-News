from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    result = find_news()

    # /**
    # Source:
    # https://stackoverflow.com/a/73050/17053855
    # */
    sort_title = sorted(result, key=lambda result: result['title'])
    sort_comments = sorted(
        sort_title,
        key=lambda sort_title: sort_title['comments_count'],
        reverse=True
    )
    limited_newlist = sort_comments[:5]

    # /**
    # * Consultei o repositório do
    # Lucas Dalbo (Lucas-Dalbo) para resolver essa parte.
    # * Link do repositório:
    # * https://github.com/tryber/sd-020-a-tech-news/pull/2
    # */
    list_tuple = [(item["title"], item["url"]) for item in limited_newlist]

    return list_tuple


# Requisito 11
def top_5_categories():
    result = find_news()
    categories = [item["category"] for item in result]
    sorted_categories = sorted(categories)
    sorted_alphabetically = Counter(sorted_categories)
    most_common = sorted_alphabetically.most_common(5)

    list_of_categories = []
    for index in most_common:
        list_of_categories.append(index[0])

    print(list_of_categories)
    return list_of_categories
